GROBID_ZIP=grobid-grobid-parent-0.4.1.zip
GROBID_FOLDER=grobid-grobid-parent-0.4.1
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

GROBID_PARENT_ZIP_URL=https://github.com/kermitt2/grobid/releases/download/grobid-parent-0.4.1/grobid-grobid-parent-0.4.1.zip

if [ ! -f $SCRIPT_DIR/../$GROBID_ZIP ]; then
  echo Downloading $GROBID_PARENT_ZIP_URL
  curl -L $GROBID_PARENT_ZIP_URL > $SCRIPT_DIR/../$GROBID_ZIP
fi

if [ ! -d $SCRIPT_DIR/../$GROBID_FOLDER ]; then
  echo Extracting the grobid-parent-0.4.1 .zip file
  unzip $SCRIPT_DIR/../$GROBID_ZIP -d $SCRIPT_DIR/../
fi

echo Done!
