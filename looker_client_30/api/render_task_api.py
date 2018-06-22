# coding: utf-8

"""
    Looker API 3.0 Reference

    ### Authorization  The Looker API uses Looker **API3** credentials for authorization and access control. Looker admins can create API3 credentials on Looker's **Admin/Users** page. Pass API3 credentials to the **/login** endpoint to obtain a temporary access_token. Include that access_token in the Authorization header of Looker API requests. For details, see [Looker API Authorization](https://looker.com/docs/r/api/authorization)  ### Client SDKs  The Looker API is a RESTful system that should be usable by any programming language capable of making HTTPS requests. Client SDKs for a variety of programming languages can be generated from the Looker API's Swagger JSON metadata to streamline use of the Looker API in your applications. A client SDK for Ruby is available as an example. For more information, see [Looker API Client SDKs](https://looker.com/docs/r/api/client_sdks)  ### Try It Out!  The 'api-docs' page served by the Looker instance includes 'Try It Out!' buttons for each API method. After logging in with API3 credentials, you can use the \"Try It Out!\" buttons to call the API directly from the documentation page to interactively explore API features and responses.  ### Versioning  Future releases of Looker will expand this API release-by-release to securely expose more and more of the core power of Looker to API client applications. API endpoints marked as \"beta\" may receive breaking changes without warning. Stable (non-beta) API endpoints should not receive breaking changes in future releases. For more information, see [Looker API Versioning](https://looker.com/docs/r/api/versioning)   # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from looker_client_30.api_client import ApiClient


class RenderTaskApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_dashboard_render_task(self, dashboard_id, result_format, body, width, height, **kwargs):  # noqa: E501
        """Create Dashboard Render Task  # noqa: E501

        ### Create a new task to render a dashboard to a document or image.  Returns a render task object. To check the status of a render task, pass the render_task.id to [Get Render Task](#!/RenderTask/get_render_task). Once the render task is complete, you can download the resulting document or image using [Get Render Task Results](#!/RenderTask/get_render_task_results).    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_dashboard_render_task(dashboard_id, result_format, body, width, height, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dashboard_id: Id of dashboard to render (required)
        :param str result_format: Output type: pdf, png, or jpg (required)
        :param CreateDashboardRenderTask body: Dashboard render task parameters (required)
        :param int width: Output width in pixels (required)
        :param int height: Output height in pixels (required)
        :param str fields: Requested fields.
        :return: RenderTask
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_dashboard_render_task_with_http_info(dashboard_id, result_format, body, width, height, **kwargs)  # noqa: E501
        else:
            (data) = self.create_dashboard_render_task_with_http_info(dashboard_id, result_format, body, width, height, **kwargs)  # noqa: E501
            return data

    def create_dashboard_render_task_with_http_info(self, dashboard_id, result_format, body, width, height, **kwargs):  # noqa: E501
        """Create Dashboard Render Task  # noqa: E501

        ### Create a new task to render a dashboard to a document or image.  Returns a render task object. To check the status of a render task, pass the render_task.id to [Get Render Task](#!/RenderTask/get_render_task). Once the render task is complete, you can download the resulting document or image using [Get Render Task Results](#!/RenderTask/get_render_task_results).    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_dashboard_render_task_with_http_info(dashboard_id, result_format, body, width, height, async=True)
        >>> result = thread.get()

        :param async bool
        :param int dashboard_id: Id of dashboard to render (required)
        :param str result_format: Output type: pdf, png, or jpg (required)
        :param CreateDashboardRenderTask body: Dashboard render task parameters (required)
        :param int width: Output width in pixels (required)
        :param int height: Output height in pixels (required)
        :param str fields: Requested fields.
        :return: RenderTask
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dashboard_id', 'result_format', 'body', 'width', 'height', 'fields']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_dashboard_render_task" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dashboard_id' is set
        if ('dashboard_id' not in params or
                params['dashboard_id'] is None):
            raise ValueError("Missing the required parameter `dashboard_id` when calling `create_dashboard_render_task`")  # noqa: E501
        # verify the required parameter 'result_format' is set
        if ('result_format' not in params or
                params['result_format'] is None):
            raise ValueError("Missing the required parameter `result_format` when calling `create_dashboard_render_task`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_dashboard_render_task`")  # noqa: E501
        # verify the required parameter 'width' is set
        if ('width' not in params or
                params['width'] is None):
            raise ValueError("Missing the required parameter `width` when calling `create_dashboard_render_task`")  # noqa: E501
        # verify the required parameter 'height' is set
        if ('height' not in params or
                params['height'] is None):
            raise ValueError("Missing the required parameter `height` when calling `create_dashboard_render_task`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dashboard_id' in params:
            path_params['dashboard_id'] = params['dashboard_id']  # noqa: E501
        if 'result_format' in params:
            path_params['result_format'] = params['result_format']  # noqa: E501

        query_params = []
        if 'width' in params:
            query_params.append(('width', params['width']))  # noqa: E501
        if 'height' in params:
            query_params.append(('height', params['height']))  # noqa: E501
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/render_tasks/dashboards/{dashboard_id}/{result_format}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RenderTask',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_look_render_task(self, look_id, result_format, width, height, **kwargs):  # noqa: E501
        """Create Look Render Task  # noqa: E501

        ### Create a new task to render a look to an image.  Returns a render task object. To check the status of a render task, pass the render_task.id to [Get Render Task](#!/RenderTask/get_render_task). Once the render task is complete, you can download the resulting document or image using [Get Render Task Results](#!/RenderTask/get_render_task_results).    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_look_render_task(look_id, result_format, width, height, async=True)
        >>> result = thread.get()

        :param async bool
        :param int look_id: Id of look to render (required)
        :param str result_format: Output type: png, or jpg (required)
        :param int width: Output width in pixels (required)
        :param int height: Output height in pixels (required)
        :param str fields: Requested fields.
        :return: RenderTask
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_look_render_task_with_http_info(look_id, result_format, width, height, **kwargs)  # noqa: E501
        else:
            (data) = self.create_look_render_task_with_http_info(look_id, result_format, width, height, **kwargs)  # noqa: E501
            return data

    def create_look_render_task_with_http_info(self, look_id, result_format, width, height, **kwargs):  # noqa: E501
        """Create Look Render Task  # noqa: E501

        ### Create a new task to render a look to an image.  Returns a render task object. To check the status of a render task, pass the render_task.id to [Get Render Task](#!/RenderTask/get_render_task). Once the render task is complete, you can download the resulting document or image using [Get Render Task Results](#!/RenderTask/get_render_task_results).    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_look_render_task_with_http_info(look_id, result_format, width, height, async=True)
        >>> result = thread.get()

        :param async bool
        :param int look_id: Id of look to render (required)
        :param str result_format: Output type: png, or jpg (required)
        :param int width: Output width in pixels (required)
        :param int height: Output height in pixels (required)
        :param str fields: Requested fields.
        :return: RenderTask
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['look_id', 'result_format', 'width', 'height', 'fields']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_look_render_task" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'look_id' is set
        if ('look_id' not in params or
                params['look_id'] is None):
            raise ValueError("Missing the required parameter `look_id` when calling `create_look_render_task`")  # noqa: E501
        # verify the required parameter 'result_format' is set
        if ('result_format' not in params or
                params['result_format'] is None):
            raise ValueError("Missing the required parameter `result_format` when calling `create_look_render_task`")  # noqa: E501
        # verify the required parameter 'width' is set
        if ('width' not in params or
                params['width'] is None):
            raise ValueError("Missing the required parameter `width` when calling `create_look_render_task`")  # noqa: E501
        # verify the required parameter 'height' is set
        if ('height' not in params or
                params['height'] is None):
            raise ValueError("Missing the required parameter `height` when calling `create_look_render_task`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'look_id' in params:
            path_params['look_id'] = params['look_id']  # noqa: E501
        if 'result_format' in params:
            path_params['result_format'] = params['result_format']  # noqa: E501

        query_params = []
        if 'width' in params:
            query_params.append(('width', params['width']))  # noqa: E501
        if 'height' in params:
            query_params.append(('height', params['height']))  # noqa: E501
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/render_tasks/looks/{look_id}/{result_format}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RenderTask',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_lookml_dashboard_render_task(self, dashboard_id, result_format, body, width, height, **kwargs):  # noqa: E501
        """Create Lookml Dashboard Render Task  # noqa: E501

        ### Create a new task to render a lookml dashboard to a document or image.  Returns a render task object. To check the status of a render task, pass the render_task.id to [Get Render Task](#!/RenderTask/get_render_task). Once the render task is complete, you can download the resulting document or image using [Get Render Task Results](#!/RenderTask/get_render_task_results).    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_lookml_dashboard_render_task(dashboard_id, result_format, body, width, height, async=True)
        >>> result = thread.get()

        :param async bool
        :param str dashboard_id: Id of lookml dashboard to render (required)
        :param str result_format: Output type: pdf, png, or jpg (required)
        :param CreateDashboardRenderTask body: Dashboard render task parameters (required)
        :param int width: Output width in pixels (required)
        :param int height: Output height in pixels (required)
        :param str fields: Requested fields.
        :return: RenderTask
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_lookml_dashboard_render_task_with_http_info(dashboard_id, result_format, body, width, height, **kwargs)  # noqa: E501
        else:
            (data) = self.create_lookml_dashboard_render_task_with_http_info(dashboard_id, result_format, body, width, height, **kwargs)  # noqa: E501
            return data

    def create_lookml_dashboard_render_task_with_http_info(self, dashboard_id, result_format, body, width, height, **kwargs):  # noqa: E501
        """Create Lookml Dashboard Render Task  # noqa: E501

        ### Create a new task to render a lookml dashboard to a document or image.  Returns a render task object. To check the status of a render task, pass the render_task.id to [Get Render Task](#!/RenderTask/get_render_task). Once the render task is complete, you can download the resulting document or image using [Get Render Task Results](#!/RenderTask/get_render_task_results).    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_lookml_dashboard_render_task_with_http_info(dashboard_id, result_format, body, width, height, async=True)
        >>> result = thread.get()

        :param async bool
        :param str dashboard_id: Id of lookml dashboard to render (required)
        :param str result_format: Output type: pdf, png, or jpg (required)
        :param CreateDashboardRenderTask body: Dashboard render task parameters (required)
        :param int width: Output width in pixels (required)
        :param int height: Output height in pixels (required)
        :param str fields: Requested fields.
        :return: RenderTask
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['dashboard_id', 'result_format', 'body', 'width', 'height', 'fields']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_lookml_dashboard_render_task" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'dashboard_id' is set
        if ('dashboard_id' not in params or
                params['dashboard_id'] is None):
            raise ValueError("Missing the required parameter `dashboard_id` when calling `create_lookml_dashboard_render_task`")  # noqa: E501
        # verify the required parameter 'result_format' is set
        if ('result_format' not in params or
                params['result_format'] is None):
            raise ValueError("Missing the required parameter `result_format` when calling `create_lookml_dashboard_render_task`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_lookml_dashboard_render_task`")  # noqa: E501
        # verify the required parameter 'width' is set
        if ('width' not in params or
                params['width'] is None):
            raise ValueError("Missing the required parameter `width` when calling `create_lookml_dashboard_render_task`")  # noqa: E501
        # verify the required parameter 'height' is set
        if ('height' not in params or
                params['height'] is None):
            raise ValueError("Missing the required parameter `height` when calling `create_lookml_dashboard_render_task`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dashboard_id' in params:
            path_params['dashboard_id'] = params['dashboard_id']  # noqa: E501
        if 'result_format' in params:
            path_params['result_format'] = params['result_format']  # noqa: E501

        query_params = []
        if 'width' in params:
            query_params.append(('width', params['width']))  # noqa: E501
        if 'height' in params:
            query_params.append(('height', params['height']))  # noqa: E501
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/render_tasks/lookml_dashboards/{dashboard_id}/{result_format}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RenderTask',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_query_render_task(self, query_id, result_format, width, height, **kwargs):  # noqa: E501
        """Create Query Render Task  # noqa: E501

        ### Create a new task to render an existing query to an image.  Returns a render task object. To check the status of a render task, pass the render_task.id to [Get Render Task](#!/RenderTask/get_render_task). Once the render task is complete, you can download the resulting document or image using [Get Render Task Results](#!/RenderTask/get_render_task_results).    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_query_render_task(query_id, result_format, width, height, async=True)
        >>> result = thread.get()

        :param async bool
        :param int query_id: Id of the query to render (required)
        :param str result_format: Output type: png or jpg (required)
        :param int width: Output width in pixels (required)
        :param int height: Output height in pixels (required)
        :param str fields: Requested fields.
        :return: RenderTask
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_query_render_task_with_http_info(query_id, result_format, width, height, **kwargs)  # noqa: E501
        else:
            (data) = self.create_query_render_task_with_http_info(query_id, result_format, width, height, **kwargs)  # noqa: E501
            return data

    def create_query_render_task_with_http_info(self, query_id, result_format, width, height, **kwargs):  # noqa: E501
        """Create Query Render Task  # noqa: E501

        ### Create a new task to render an existing query to an image.  Returns a render task object. To check the status of a render task, pass the render_task.id to [Get Render Task](#!/RenderTask/get_render_task). Once the render task is complete, you can download the resulting document or image using [Get Render Task Results](#!/RenderTask/get_render_task_results).    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_query_render_task_with_http_info(query_id, result_format, width, height, async=True)
        >>> result = thread.get()

        :param async bool
        :param int query_id: Id of the query to render (required)
        :param str result_format: Output type: png or jpg (required)
        :param int width: Output width in pixels (required)
        :param int height: Output height in pixels (required)
        :param str fields: Requested fields.
        :return: RenderTask
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query_id', 'result_format', 'width', 'height', 'fields']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_query_render_task" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query_id' is set
        if ('query_id' not in params or
                params['query_id'] is None):
            raise ValueError("Missing the required parameter `query_id` when calling `create_query_render_task`")  # noqa: E501
        # verify the required parameter 'result_format' is set
        if ('result_format' not in params or
                params['result_format'] is None):
            raise ValueError("Missing the required parameter `result_format` when calling `create_query_render_task`")  # noqa: E501
        # verify the required parameter 'width' is set
        if ('width' not in params or
                params['width'] is None):
            raise ValueError("Missing the required parameter `width` when calling `create_query_render_task`")  # noqa: E501
        # verify the required parameter 'height' is set
        if ('height' not in params or
                params['height'] is None):
            raise ValueError("Missing the required parameter `height` when calling `create_query_render_task`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'query_id' in params:
            path_params['query_id'] = params['query_id']  # noqa: E501
        if 'result_format' in params:
            path_params['result_format'] = params['result_format']  # noqa: E501

        query_params = []
        if 'width' in params:
            query_params.append(('width', params['width']))  # noqa: E501
        if 'height' in params:
            query_params.append(('height', params['height']))  # noqa: E501
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/render_tasks/queries/{query_id}/{result_format}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RenderTask',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def render_task(self, render_task_id, **kwargs):  # noqa: E501
        """Get Render Task  # noqa: E501

        ### Get information about a render task.  Returns a render task object. To check the status of a render task, pass the render_task.id to [Get Render Task](#!/RenderTask/get_render_task). Once the render task is complete, you can download the resulting document or image using [Get Render Task Results](#!/RenderTask/get_render_task_results).    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.render_task(render_task_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str render_task_id: Id of render task (required)
        :param str fields: Requested fields.
        :return: RenderTask
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.render_task_with_http_info(render_task_id, **kwargs)  # noqa: E501
        else:
            (data) = self.render_task_with_http_info(render_task_id, **kwargs)  # noqa: E501
            return data

    def render_task_with_http_info(self, render_task_id, **kwargs):  # noqa: E501
        """Get Render Task  # noqa: E501

        ### Get information about a render task.  Returns a render task object. To check the status of a render task, pass the render_task.id to [Get Render Task](#!/RenderTask/get_render_task). Once the render task is complete, you can download the resulting document or image using [Get Render Task Results](#!/RenderTask/get_render_task_results).    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.render_task_with_http_info(render_task_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str render_task_id: Id of render task (required)
        :param str fields: Requested fields.
        :return: RenderTask
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['render_task_id', 'fields']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method render_task" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'render_task_id' is set
        if ('render_task_id' not in params or
                params['render_task_id'] is None):
            raise ValueError("Missing the required parameter `render_task_id` when calling `render_task`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'render_task_id' in params:
            path_params['render_task_id'] = params['render_task_id']  # noqa: E501

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/render_tasks/{render_task_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RenderTask',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def render_task_results(self, render_task_id, **kwargs):  # noqa: E501
        """Render Task Results  # noqa: E501

        ### Get the document or image produced by a completed render task.  Returns `102 Processing` if the render task has not completed.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.render_task_results(render_task_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str render_task_id: Id of render task (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.render_task_results_with_http_info(render_task_id, **kwargs)  # noqa: E501
        else:
            (data) = self.render_task_results_with_http_info(render_task_id, **kwargs)  # noqa: E501
            return data

    def render_task_results_with_http_info(self, render_task_id, **kwargs):  # noqa: E501
        """Render Task Results  # noqa: E501

        ### Get the document or image produced by a completed render task.  Returns `102 Processing` if the render task has not completed.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.render_task_results_with_http_info(render_task_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str render_task_id: Id of render task (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['render_task_id', 'result_format']  # Added result_format to handle file downloads
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method render_task_results" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'render_task_id' is set
        if ('render_task_id' not in params or
                params['render_task_id'] is None):
            raise ValueError("Missing the required parameter `render_task_id` when calling `render_task_results`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'render_task_id' in params:
            path_params['render_task_id'] = params['render_task_id']  # noqa: E501
            
        # Add handling for result_format to swagger-codegen code
        if 'result_format' in params:
            if params['result_format'] in ['pdf', 'png', 'jpg']:
                result_format = 'file'
            else:
                result_format = 'str'
        else:
            result_format = 'str'

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['image/jpeg', 'image/png', 'application/pdf'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/render_tasks/{render_task_id}/results', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=result_format,  # changed from swagger_codegen
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
