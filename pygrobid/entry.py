import subprocess
import os
import time

from py4j.java_gateway import JavaGateway


def start_server():
    MAX_WAIT_TIME_FOR_JAVA_SERVER = 3
    here = os.path.abspath(os.path.dirname(__file__))
    p = subprocess.Popen(['mvn exec:exec -Pstart_grobid'],
                         cwd=here,
                         shell=True,
                         stdin=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdout = subprocess.PIPE)
    time.sleep(MAX_WAIT_TIME_FOR_JAVA_SERVER)


class Grobid():

    def __init__(self):
        self._gateway = JavaGateway()
        self._grobid_engine = self._gateway.entry_point.getEngine()

    def shutdown(self):
        self._gateway.shutdown()

    def process_authors_header(self, author_sequence):
        return self._grobid_engine.processAuthorsHeader(author_sequence)

    def process_authors_citation(self, author_sequence):
        return self._grobid_engine.processAuthorsCitation(author_sequence)

    def process_affiliation(self, address_block):
        return self._grobid_engine.processAffiliation(address_block)

    def process_raw_reference(self, reference_str, consolidate=False):
        """
        * Apply a parsing model for a given single raw reference string based on
        * CRF
        *
        * @param reference   : the reference string to be processed
        * @param consolidate - the consolidation option allows GROBID to exploit Crossref
        *                    web services for improving header information
        * @return the recognized bibliographical object
        """
        return self._grobid_engine.processRawReference(reference_str, consolidate)

    def process_references(self, filepath, consolidate=False):
        """
        * Apply a parsing model to the reference block of a PDF file based on CRF
        *
        * @param inputFile   : the path of the PDF file to be processed
        * @param consolidate - the consolidation option allows GROBID to exploit Crossref
        *                    web services for improving header information
        * @return the list of parsed references as bibliographical objects enriched
        *         with citation contexts
        """
        input_file = self._gateway.jvm.java.io.File(filepath)
        return self._grobid_engine.processReferences(input_file, consolidate)

    def process_header(self, input_file, consolidate=False):
        """
        * Apply a parsing model for the header of a PDF file based on CRF, using
        * first three pages of the PDF
        *
        * @param inputFile   : the path of the PDF file to be processed
        * @param consolidate - the consolidation option allows GROBID to exploit Crossref
        *                    web services for improving header information
        * @param result      bib result
        * @return the TEI representation of the extracted bibliographical
        *         information
        """
        result = self._gateway.entry_point.biblioItem()
        return self._grobid_engine.processHeader(input_file, consolidate, result)

    @property
    def accepted_languages(self):
        return self._grobid_engine.getAcceptedLanguages()
