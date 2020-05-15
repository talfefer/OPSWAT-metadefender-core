=begin comment

MetaDefender Core

## Developer Guide This is the API documentation for *MetaDefender Core Public API*.  If you would like to evaluate or have any questions about this documentation, please contact us via our [Contact Us](https://opswat.com/contact) form.  ## How to Interact with MetaDefender Core using REST Beginning with MetaDefender Core 4.x, OPSWAT recommends using the JSON-based REST API. The available methods are documented below. > _**Note**:_ MetaDefender API doesn't support chunk upload, however is recommended to stream the files to MetaDefender as part of the upload process.  --- ## File Analysis Process    MetaDefender's main functionality is to analyze large volumes with a high throughput. Depending on the configuration and licensed technologies, the analysis times can vary.    Below is a brief description of the API integration flow:    1. Upload a file for analysis (`POST /file`), which returns the `data_id`: [File Analysis](#operation/fileAnalysisPost)).           > _**Note**:_ The performance depends on:           > - number of nodes (scaling)     > - number of engines per node     > - type of file to be scanned     > - Metadefender Core and nodes' hardware       2. You have 2 ways to retrieve the analysis report:      - **Polling**: Fetch the result with previously received data_id (`GET /file/{data_id}` resource) until scan result belonging to data_id doesn't reach the 100 percent progress_percentage: ( [Fetch processing result](#operation/userLogin))        > _**Note**:_ Too many data_id requests can reduce performance. It is enough to just check every few hundred milliseconds.          - **Callbackurl**: Specify a callbackurl that will be called once the analysis is complete.     3. Retrieve the analysis results anytime after the analysis is completed with hash for files (md5, sha1, sha256) by calling [Fetch processing result](#operation/userLogin).      - The hash can be found in the scan results    4. Retrieve processed file (sanitized, redacted, watermarked, etc.) after the analysis is complete.      > _**Note**:_ Based on the configured retention policy, the files might be available for retrieval at a later time.   --- OPSWAT provides some sample codes on [GitHub](https://github.com/OPSWAT) to make it easier to understand how the MetaDefender REST API works. 

The version of the OpenAPI document: v4.18.0
Contact: feedback@opswat.com
Generated by: https://openapi-generator.tech

=end comment

=cut

#
# NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
# Do not edit the class manually.
# Ref: https://openapi-generator.tech
#
package WWW::OpenAPIClient::LicenseApi;

require 5.6.0;
use strict;
use warnings;
use utf8; 
use Exporter;
use Carp qw( croak );
use Log::Any qw($log);

use WWW::OpenAPIClient::ApiClient;

use base "Class::Data::Inheritable";

__PACKAGE__->mk_classdata('method_documentation' => {});

sub new {
    my $class = shift;
    my $api_client;

    if ($_[0] && ref $_[0] && ref $_[0] eq 'WWW::OpenAPIClient::ApiClient' ) {
        $api_client = $_[0];
    } else {
        $api_client = WWW::OpenAPIClient::ApiClient->new(@_);
    }

    bless { api_client => $api_client }, $class;

}


#
# license_activation
#
# Activate license
# 
# @param string $apikey Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                 (optional)
# @param UNKNOWN_BASE_TYPE $unknown_base_type  (optional)
{
    my $params = {
    'apikey' => {
        data_type => 'string',
        description => 'Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                ',
        required => '0',
    },
    'unknown_base_type' => {
        data_type => 'UNKNOWN_BASE_TYPE',
        description => '',
        required => '0',
    },
    };
    __PACKAGE__->method_documentation->{ 'license_activation' } = { 
        summary => 'Activate license',
        params => $params,
        returns => undef,
        };
}
# @return void
#
sub license_activation {
    my ($self, %args) = @_;

    # parse inputs
    my $_resource_path = '/admin/license/activation';

    my $_method = 'POST';
    my $query_params = {};
    my $header_params = {};
    my $form_params = {};

    # 'Accept' and 'Content-Type' header
    my $_header_accept = $self->{api_client}->select_header_accept('application/json');
    if ($_header_accept) {
        $header_params->{'Accept'} = $_header_accept;
    }
    $header_params->{'Content-Type'} = $self->{api_client}->select_header_content_type('application/json');

    # header params
    if ( exists $args{'apikey'}) {
        $header_params->{'apikey'} = $self->{api_client}->to_header_value($args{'apikey'});
    }

    my $_body_data;
    # body params
    if ( exists $args{'unknown_base_type'}) {
        $_body_data = $args{'unknown_base_type'};
    }

    # authentication setting, if any
    my $auth_settings = [qw(apikey )];

    # make the API Call
    $self->{api_client}->call_api($_resource_path, $_method,
                                           $query_params, $form_params,
                                           $header_params, $_body_data, $auth_settings);
    return;
}

#
# license_get
#
# Get Current License Information
# 
# @param string $apikey Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                 (optional)
{
    my $params = {
    'apikey' => {
        data_type => 'string',
        description => 'Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                ',
        required => '0',
    },
    };
    __PACKAGE__->method_documentation->{ 'license_get' } = { 
        summary => 'Get Current License Information',
        params => $params,
        returns => 'LicenseInformation',
        };
}
# @return LicenseInformation
#
sub license_get {
    my ($self, %args) = @_;

    # parse inputs
    my $_resource_path = '/admin/license';

    my $_method = 'GET';
    my $query_params = {};
    my $header_params = {};
    my $form_params = {};

    # 'Accept' and 'Content-Type' header
    my $_header_accept = $self->{api_client}->select_header_accept('application/json');
    if ($_header_accept) {
        $header_params->{'Accept'} = $_header_accept;
    }
    $header_params->{'Content-Type'} = $self->{api_client}->select_header_content_type();

    # header params
    if ( exists $args{'apikey'}) {
        $header_params->{'apikey'} = $self->{api_client}->to_header_value($args{'apikey'});
    }

    my $_body_data;
    # authentication setting, if any
    my $auth_settings = [qw(apikey )];

    # make the API Call
    my $response = $self->{api_client}->call_api($_resource_path, $_method,
                                           $query_params, $form_params,
                                           $header_params, $_body_data, $auth_settings);
    if (!$response) {
        return;
    }
    my $_response_object = $self->{api_client}->deserialize('LicenseInformation', $response);
    return $_response_object;
}

#
# license_upload
#
# Upload license key
# 
# @param string $apikey Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                 (optional)
# @param string $body  (optional)
{
    my $params = {
    'apikey' => {
        data_type => 'string',
        description => 'Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                ',
        required => '0',
    },
    'body' => {
        data_type => 'string',
        description => '',
        required => '0',
    },
    };
    __PACKAGE__->method_documentation->{ 'license_upload' } = { 
        summary => 'Upload license key',
        params => $params,
        returns => undef,
        };
}
# @return void
#
sub license_upload {
    my ($self, %args) = @_;

    # parse inputs
    my $_resource_path = '/admin/license';

    my $_method = 'POST';
    my $query_params = {};
    my $header_params = {};
    my $form_params = {};

    # 'Accept' and 'Content-Type' header
    my $_header_accept = $self->{api_client}->select_header_accept('application/json');
    if ($_header_accept) {
        $header_params->{'Accept'} = $_header_accept;
    }
    $header_params->{'Content-Type'} = $self->{api_client}->select_header_content_type('application/octet-stream');

    # header params
    if ( exists $args{'apikey'}) {
        $header_params->{'apikey'} = $self->{api_client}->to_header_value($args{'apikey'});
    }

    my $_body_data;
    # body params
    if ( exists $args{'body'}) {
        $_body_data = $args{'body'};
    }

    # authentication setting, if any
    my $auth_settings = [qw(apikey )];

    # make the API Call
    $self->{api_client}->call_api($_resource_path, $_method,
                                           $query_params, $form_params,
                                           $header_params, $_body_data, $auth_settings);
    return;
}

1;
