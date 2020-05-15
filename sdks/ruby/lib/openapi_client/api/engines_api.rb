=begin
#MetaDefender Core

### Developer Guide This is the API documentation for *MetaDefender Core Public API*.  If you would like to evaluate or have any questions about this documentation, please contact us via our [Contact Us](https://opswat.com/contact) form.  ## How to Interact with MetaDefender Core using REST Beginning with MetaDefender Core 4.x, OPSWAT recommends using the JSON-based REST API. The available methods are documented below. > _**Note**:_ MetaDefender API doesn't support chunk upload, however is recommended to stream the files to MetaDefender as part of the upload process.  --- ## File Analysis Process    MetaDefender's main functionality is to analyze large volumes with a high throughput. Depending on the configuration and licensed technologies, the analysis times can vary.    Below is a brief description of the API integration flow:    1. Upload a file for analysis (`POST /file`), which returns the `data_id`: [File Analysis](#operation/fileAnalysisPost)).           > _**Note**:_ The performance depends on:           > - number of nodes (scaling)     > - number of engines per node     > - type of file to be scanned     > - Metadefender Core and nodes' hardware       2. You have 2 ways to retrieve the analysis report:      - **Polling**: Fetch the result with previously received data_id (`GET /file/{data_id}` resource) until scan result belonging to data_id doesn't reach the 100 percent progress_percentage: ( [Fetch processing result](#operation/userLogin))        > _**Note**:_ Too many data_id requests can reduce performance. It is enough to just check every few hundred milliseconds.          - **Callbackurl**: Specify a callbackurl that will be called once the analysis is complete.     3. Retrieve the analysis results anytime after the analysis is completed with hash for files (md5, sha1, sha256) by calling [Fetch processing result](#operation/userLogin).      - The hash can be found in the scan results    4. Retrieve processed file (sanitized, redacted, watermarked, etc.) after the analysis is complete.      > _**Note**:_ Based on the configured retention policy, the files might be available for retrieval at a later time.   --- OPSWAT provides some sample codes on [GitHub](https://github.com/OPSWAT) to make it easier to understand how the MetaDefender REST API works. 

The version of the OpenAPI document: v4.18.0
Contact: feedback@opswat.com
Generated by: https://openapi-generator.tech
OpenAPI Generator version: 4.3.0

=end

require 'cgi'

module OpenapiClient
  class EnginesApi
    attr_accessor :api_client

    def initialize(api_client = ApiClient.default)
      @api_client = api_client
    end
    # Disable engines
    # Disable to use the selected engines on the nodes.
    # @param engine_id [String] The unique engine identifier
    # @param [Hash] opts the optional parameters
    # @option opts [String] :apikey Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                
    # @return [InlineResponse2005]
    def engine_disable(engine_id, opts = {})
      data, _status_code, _headers = engine_disable_with_http_info(engine_id, opts)
      data
    end

    # Disable engines
    # Disable to use the selected engines on the nodes.
    # @param engine_id [String] The unique engine identifier
    # @param [Hash] opts the optional parameters
    # @option opts [String] :apikey Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                
    # @return [Array<(InlineResponse2005, Integer, Hash)>] InlineResponse2005 data, response status code and response headers
    def engine_disable_with_http_info(engine_id, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: EnginesApi.engine_disable ...'
      end
      # verify the required parameter 'engine_id' is set
      if @api_client.config.client_side_validation && engine_id.nil?
        fail ArgumentError, "Missing the required parameter 'engine_id' when calling EnginesApi.engine_disable"
      end
      # resource path
      local_var_path = '/admin/engine/{engineId}/disable'.sub('{' + 'engineId' + '}', CGI.escape(engine_id.to_s))

      # query parameters
      query_params = opts[:query_params] || {}

      # header parameters
      header_params = opts[:header_params] || {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])
      header_params[:'apikey'] = opts[:'apikey'] if !opts[:'apikey'].nil?

      # form parameters
      form_params = opts[:form_params] || {}

      # http body (model)
      post_body = opts[:body] 

      # return_type
      return_type = opts[:return_type] || 'InlineResponse2005' 

      # auth_names
      auth_names = opts[:auth_names] || ['apikey']

      new_options = opts.merge(
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:POST, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: EnginesApi#engine_disable\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Enable engines
    # Enable to use the selected engine on the nodes.
    # @param engine_id [String] The unique engine identifier
    # @param [Hash] opts the optional parameters
    # @option opts [String] :apikey Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                
    # @return [InlineResponse2004]
    def engine_enable(engine_id, opts = {})
      data, _status_code, _headers = engine_enable_with_http_info(engine_id, opts)
      data
    end

    # Enable engines
    # Enable to use the selected engine on the nodes.
    # @param engine_id [String] The unique engine identifier
    # @param [Hash] opts the optional parameters
    # @option opts [String] :apikey Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                
    # @return [Array<(InlineResponse2004, Integer, Hash)>] InlineResponse2004 data, response status code and response headers
    def engine_enable_with_http_info(engine_id, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: EnginesApi.engine_enable ...'
      end
      # verify the required parameter 'engine_id' is set
      if @api_client.config.client_side_validation && engine_id.nil?
        fail ArgumentError, "Missing the required parameter 'engine_id' when calling EnginesApi.engine_enable"
      end
      # resource path
      local_var_path = '/admin/engine/{engineId}/enable'.sub('{' + 'engineId' + '}', CGI.escape(engine_id.to_s))

      # query parameters
      query_params = opts[:query_params] || {}

      # header parameters
      header_params = opts[:header_params] || {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])
      header_params[:'apikey'] = opts[:'apikey'] if !opts[:'apikey'].nil?

      # form parameters
      form_params = opts[:form_params] || {}

      # http body (model)
      post_body = opts[:body] 

      # return_type
      return_type = opts[:return_type] || 'InlineResponse2004' 

      # auth_names
      auth_names = opts[:auth_names] || ['apikey']

      new_options = opts.merge(
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:POST, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: EnginesApi#engine_enable\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Pin engine to prevent auto-updates
    # Pin engines to prevent applying automatic updates on them. Manual updates still can be applied.
    # @param engine_id [String] The unique engine identifier
    # @param [Hash] opts the optional parameters
    # @option opts [String] :apikey Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                
    # @option opts [String] :type Pin engine or database to prevent applying automatic updates on it. (If the type is not defined both engine and database will be pinned.)
    # @return [InlineResponse2002]
    def engine_pin(engine_id, opts = {})
      data, _status_code, _headers = engine_pin_with_http_info(engine_id, opts)
      data
    end

    # Pin engine to prevent auto-updates
    # Pin engines to prevent applying automatic updates on them. Manual updates still can be applied.
    # @param engine_id [String] The unique engine identifier
    # @param [Hash] opts the optional parameters
    # @option opts [String] :apikey Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                
    # @option opts [String] :type Pin engine or database to prevent applying automatic updates on it. (If the type is not defined both engine and database will be pinned.)
    # @return [Array<(InlineResponse2002, Integer, Hash)>] InlineResponse2002 data, response status code and response headers
    def engine_pin_with_http_info(engine_id, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: EnginesApi.engine_pin ...'
      end
      # verify the required parameter 'engine_id' is set
      if @api_client.config.client_side_validation && engine_id.nil?
        fail ArgumentError, "Missing the required parameter 'engine_id' when calling EnginesApi.engine_pin"
      end
      allowable_values = ["engine", "database"]
      if @api_client.config.client_side_validation && opts[:'type'] && !allowable_values.include?(opts[:'type'])
        fail ArgumentError, "invalid value for \"type\", must be one of #{allowable_values}"
      end
      # resource path
      local_var_path = '/admin/engine/{engineId}/pin'.sub('{' + 'engineId' + '}', CGI.escape(engine_id.to_s))

      # query parameters
      query_params = opts[:query_params] || {}

      # header parameters
      header_params = opts[:header_params] || {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])
      header_params[:'apikey'] = opts[:'apikey'] if !opts[:'apikey'].nil?
      header_params[:'type'] = opts[:'type'] if !opts[:'type'].nil?

      # form parameters
      form_params = opts[:form_params] || {}

      # http body (model)
      post_body = opts[:body] 

      # return_type
      return_type = opts[:return_type] || 'InlineResponse2002' 

      # auth_names
      auth_names = opts[:auth_names] || ['apikey']

      new_options = opts.merge(
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:POST, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: EnginesApi#engine_pin\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Unpin engine to prevent auto-updates
    # Unpin engines so automatic updates will be applied on them.
    # @param engine_id [String] The unique engine identifier
    # @param [Hash] opts the optional parameters
    # @option opts [String] :apikey Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                
    # @option opts [String] :type Unpin engine or database to applying automatic updates on it. (If it is not defined both engine and database will be unpinned.)
    # @return [InlineResponse2003]
    def engine_unpin(engine_id, opts = {})
      data, _status_code, _headers = engine_unpin_with_http_info(engine_id, opts)
      data
    end

    # Unpin engine to prevent auto-updates
    # Unpin engines so automatic updates will be applied on them.
    # @param engine_id [String] The unique engine identifier
    # @param [Hash] opts the optional parameters
    # @option opts [String] :apikey Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                
    # @option opts [String] :type Unpin engine or database to applying automatic updates on it. (If it is not defined both engine and database will be unpinned.)
    # @return [Array<(InlineResponse2003, Integer, Hash)>] InlineResponse2003 data, response status code and response headers
    def engine_unpin_with_http_info(engine_id, opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: EnginesApi.engine_unpin ...'
      end
      # verify the required parameter 'engine_id' is set
      if @api_client.config.client_side_validation && engine_id.nil?
        fail ArgumentError, "Missing the required parameter 'engine_id' when calling EnginesApi.engine_unpin"
      end
      allowable_values = ["engine", "database"]
      if @api_client.config.client_side_validation && opts[:'type'] && !allowable_values.include?(opts[:'type'])
        fail ArgumentError, "invalid value for \"type\", must be one of #{allowable_values}"
      end
      # resource path
      local_var_path = '/admin/engine/{engineId}/unpin'.sub('{' + 'engineId' + '}', CGI.escape(engine_id.to_s))

      # query parameters
      query_params = opts[:query_params] || {}

      # header parameters
      header_params = opts[:header_params] || {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])
      header_params[:'apikey'] = opts[:'apikey'] if !opts[:'apikey'].nil?
      header_params[:'type'] = opts[:'type'] if !opts[:'type'].nil?

      # form parameters
      form_params = opts[:form_params] || {}

      # http body (model)
      post_body = opts[:body] 

      # return_type
      return_type = opts[:return_type] || 'InlineResponse2003' 

      # auth_names
      auth_names = opts[:auth_names] || ['apikey']

      new_options = opts.merge(
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:POST, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: EnginesApi#engine_unpin\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end
  end
end
