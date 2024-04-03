from .utils.de_utils import convert as convert_

URI = "https://www.opengeodata.nrw.de/produkte/umwelt_klima/bodennutzung/landwirtschaft/LFK-AKTI_EPSG25832_Shape.zip"
ID = "de_nrw"
TITLE = "Field boundaries for North Rhine-Westphalia (NRW), Germany"
DESCRIPTION = """A field block (German: "Feldblock") is a contiguous agricultural area surrounded by permanent boundaries, which is cultivated by one or more farmers with one or more crops, is fully or partially set aside or is fully or partially taken out of production. Field blocks are classified separately according to the main land uses of arable land, grassland, permanent crops, 2nd pillar and other. Since 2005, field blocks in NRW have represented the area reference within the framework of the Integrated Administration and Control System (IACS) for EU agricultural subsidies."""
BBOX = [5.8659988131,50.3226989435,9.4476584861,52.5310351488]
EXTENSIONS = ["https://fiboa.github.io/inspire-extension/v0.1.0/schema.yaml"]
COLUMNS = {
    'geometry': 'geometry',
    'ID': 'id',
    'INSPIRE_ID': 'inspire:id',
    'FLIK': 'flik',
    'GUELT_VON': 'determination_datetime',
    'NUTZ_CODE': 'nutz_code',
    'NUTZ_TXT': 'nutz_txt',
    'AREA_HA': 'area'
}
MISSING_SCHEMAS = {
    'flik': {
        'type': 'string',
        'required': True
    },
    'nutz_code': {
        'type': 'string'
    },
    'nutz_txt': {
        'type': 'string'
    }
}

def convert(output_file, cache_file = None):
    """
    Converts the DE NRW field boundary datasets to fiboa.
    """
    convert_(output_file, cache_file, URI, COLUMNS, ID, TITLE, DESCRIPTION, BBOX, EXTENSIONS, MISSING_SCHEMAS)