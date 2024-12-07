from aiohttp.web import Request
from aiohttp.web_exceptions import HTTPBadRequest


def get_int_path_param(request: Request, path_param_name: str, required=True) -> int:
    try:
        raw_param = request.match_info[path_param_name]

        if len(raw_param) > 5:
            raise HTTPBadRequest(text=f"invalid param {path_param_name}")
        
        return int(raw_param)
    except KeyError:
        if required:
            raise HTTPBadRequest(text=f"missing param {path_param_name}")
        
        return None
    except ValueError:
        raise HTTPBadRequest(text=f"invalid param {path_param_name}")


def get_int_query_param(request: Request, query_param_name: str, default: int | None, required=True) -> int:
    try:
        raw_param = request.query[query_param_name]

        if len(raw_param) > 5:
            raise HTTPBadRequest(text=f"invalid param {query_param_name}")
        
        return int(raw_param)
    except KeyError:
        if required:
            if default is not None:
                return default
            
            raise HTTPBadRequest(text=f"missing param {query_param_name}")
        
        return None
    except ValueError:
        raise HTTPBadRequest(text=f"invalid param {query_param_name}")


def get_str_query_param(request: Request, query_param_name: str, default: str | None, required=True) -> str:
    try:
        raw_param = request.query[query_param_name]

        if len(raw_param) > 128:
            raise HTTPBadRequest(text=f"invalid param {query_param_name}")
        
        return raw_param
    except KeyError:
        if required:
            if default is not None:
                return default
            
            raise HTTPBadRequest(text=f"missing param {query_param_name}")
        
        return None
    except ValueError:
        raise HTTPBadRequest(text=f"invalid param {query_param_name}")
