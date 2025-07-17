import azure.functions as func
import logging

from wall_type_explainer import get_wall_type_descriptions

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.function_name(name="wallTypeExplainer")
@app.route(route="describe/wall-types", methods=["POST"])
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
        wall_codes = req_body["wallCodes"]

        result = get_wall_type_descriptions(wall_codes)
        return func.HttpResponse(result, status_code=200, mimetype="application/json")
    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
