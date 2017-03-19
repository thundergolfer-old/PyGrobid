/**
 * Created by jbelotti on 19/3/17.
 */
import org.grobid.core.engines.Engine;
import org.grobid.core.factory.GrobidFactory;
import org.grobid.core.mock.MockContext;
import org.grobid.core.utilities.GrobidProperties;
import org.slf4j.impl.SimpleLogger;
import py4j.GatewayServer;

import java.nio.file.Paths;
import java.nio.file.Path;

public class GrobidEntryPoint {

    private Engine engine;

    public GrobidEntryPoint() {

        System.out.println("Working Directory = " + System.getProperty("user.dir"));

        String pdfPath = "mypdffile.pdf";

        try {
            String pGrobidHome = "grobid-grobid-parent-0.4.1/grobid-home/";
            String pGrobidProperties = "grobid-grobid-parent-0.4.1/grobid-home/config/grobid.properties";

            try {
                MockContext.setInitialContext(pGrobidHome, pGrobidProperties);
            } catch (Exception e1) {
                e1.printStackTrace();
            }

            GrobidProperties.getInstance();

//            System.out.println(">>>>>>>> GROBID_HOME="+GrobidProperties.get_GROBID_HOME_PATH());

            engine = GrobidFactory.getInstance().createEngine();

            // Biblio object for the result
//            BiblioItem resHeader = new BiblioItem();
//            String tei = engine.processHeader(pdfPath, false, resHeader);
        }
        catch (Exception e) {
            // If an exception is generated, print a stack trace
            e.printStackTrace();
        }
        finally {
            try {
                MockContext.destroyInitialContext();
            }
            catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) {
        GatewayServer gatewayServer = new GatewayServer(new GrobidEntryPoint());
        gatewayServer.start();
        System.out.println("Grobid Gateway Server Started");
    }

}
