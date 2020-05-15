=begin comment

MetaDefender Core

## Developer Guide This is the API documentation for *MetaDefender Core Public API*.  If you would like to evaluate or have any questions about this documentation, please contact us via our [Contact Us](https://opswat.com/contact) form.  ## How to Interact with MetaDefender Core using REST Beginning with MetaDefender Core 4.x, OPSWAT recommends using the JSON-based REST API. The available methods are documented below. > _**Note**:_ MetaDefender API doesn't support chunk upload, however is recommended to stream the files to MetaDefender as part of the upload process.  --- ## File Analysis Process    MetaDefender's main functionality is to analyze large volumes with a high throughput. Depending on the configuration and licensed technologies, the analysis times can vary.    Below is a brief description of the API integration flow:    1. Upload a file for analysis (`POST /file`), which returns the `data_id`: [File Analysis](#operation/fileAnalysisPost)).           > _**Note**:_ The performance depends on:           > - number of nodes (scaling)     > - number of engines per node     > - type of file to be scanned     > - Metadefender Core and nodes' hardware       2. You have 2 ways to retrieve the analysis report:      - **Polling**: Fetch the result with previously received data_id (`GET /file/{data_id}` resource) until scan result belonging to data_id doesn't reach the 100 percent progress_percentage: ( [Fetch processing result](#operation/userLogin))        > _**Note**:_ Too many data_id requests can reduce performance. It is enough to just check every few hundred milliseconds.          - **Callbackurl**: Specify a callbackurl that will be called once the analysis is complete.     3. Retrieve the analysis results anytime after the analysis is completed with hash for files (md5, sha1, sha256) by calling [Fetch processing result](#operation/userLogin).      - The hash can be found in the scan results    4. Retrieve processed file (sanitized, redacted, watermarked, etc.) after the analysis is complete.      > _**Note**:_ Based on the configured retention policy, the files might be available for retrieval at a later time.   --- OPSWAT provides some sample codes on [GitHub](https://github.com/OPSWAT) to make it easier to understand how the MetaDefender REST API works. 

The version of the OpenAPI document: v4.18.0
Contact: feedback@opswat.com
Generated by: https://openapi-generator.tech

=end comment

=cut

#
# NOTE: This class is auto generated by OpenAPI Generator
# Please update the test cases below to test the API endpoints.
# Ref: https://openapi-generator.tech
#
use Test::More tests => 1; #TODO update number of test cases
use Test::Exception;

use lib 'lib';
use strict;
use warnings;

use_ok('WWW::OpenAPIClient::ConfigApi');

my $api = WWW::OpenAPIClient::ConfigApi->new();
isa_ok($api, 'WWW::OpenAPIClient::ConfigApi');

#
# config_audit_log test
#
{
    my $apikey = undef; # replace NULL with a proper value
    my $unknown_base_type = undef; # replace NULL with a proper value
    my $result = $api->config_audit_log(apikey => $apikey, unknown_base_type => $unknown_base_type);
}

#
# config_get_skip_hash test
#
{
    my $apikey = undef; # replace NULL with a proper value
    my $result = $api->config_get_skip_hash(apikey => $apikey);
}

#
# config_quarantine test
#
{
    my $apikey = undef; # replace NULL with a proper value
    my $unknown_base_type = undef; # replace NULL with a proper value
    my $result = $api->config_quarantine(apikey => $apikey, unknown_base_type => $unknown_base_type);
}

#
# config_sanitized_repo test
#
{
    my $apikey = undef; # replace NULL with a proper value
    my $inline_object1 = undef; # replace NULL with a proper value
    my $result = $api->config_sanitized_repo(apikey => $apikey, inline_object1 => $inline_object1);
}

#
# config_scan_history test
#
{
    my $apikey = undef; # replace NULL with a proper value
    my $unknown_base_type = undef; # replace NULL with a proper value
    my $result = $api->config_scan_history(apikey => $apikey, unknown_base_type => $unknown_base_type);
}

#
# config_session test
#
{
    my $apikey = undef; # replace NULL with a proper value
    my $admin_config_session = undef; # replace NULL with a proper value
    my $result = $api->config_session(apikey => $apikey, admin_config_session => $admin_config_session);
}

#
# config_update test
#
{
    my $apikey = undef; # replace NULL with a proper value
    my $admin_config_update = undef; # replace NULL with a proper value
    my $result = $api->config_update(apikey => $apikey, admin_config_update => $admin_config_update);
}

#
# config_update_skip_hash test
#
{
    my $apikey = undef; # replace NULL with a proper value
    my $skip_list = undef; # replace NULL with a proper value
    my $result = $api->config_update_skip_hash(apikey => $apikey, skip_list => $skip_list);
}

#
# config_update_webhook test
#
{
    my $apikey = undef; # replace NULL with a proper value
    my $admin_config_webhook = undef; # replace NULL with a proper value
    my $result = $api->config_update_webhook(apikey => $apikey, admin_config_webhook => $admin_config_webhook);
}

#
# config_webhook test
#
{
    my $apikey = undef; # replace NULL with a proper value
    my $result = $api->config_webhook(apikey => $apikey);
}


1;
