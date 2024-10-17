class InvalidDestData(Exception):
    """Invalid destination data"""
    pass

class InvalidHeaderData(Exception):
    """Invalid header payload"""
    pass

class InvalidHeaderProtocol(Exception):
    """Protocol doesn't match BUDP"""
    pass


class InvalidHeaderSize(Exception):
    """Current header size doesn't match predesignated header size"""
