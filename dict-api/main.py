import api, api_documentation
import justpy as jp

jp.Route('/api',api.API.serve)
jp.Route('/',api_documentation.Docs.serve)
jp.justpy()