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
package WWW::OpenAPIClient::Object::DLPResponseDlpInfo;

require 5.6.0;
use strict;
use warnings;
use utf8;
use JSON qw(decode_json);
use Data::Dumper;
use Module::Runtime qw(use_module);
use Log::Any qw($log);
use Date::Parse;
use DateTime;

use WWW::OpenAPIClient::Object::DLPResponseDlpInfoHits;
use WWW::OpenAPIClient::Object::DLPResponseDlpInfoMetadataRemoval;
use WWW::OpenAPIClient::Object::DLPResponseDlpInfoRedact;
use WWW::OpenAPIClient::Object::DLPResponseDlpInfoWatermark;

use base ("Class::Accessor", "Class::Data::Inheritable");

#
#Information on matched sensitive data
#
# NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech). Do not edit the class manually.
# REF: https://openapi-generator.tech
#

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
__PACKAGE__->mk_classdata('attribute_map' => {});
__PACKAGE__->mk_classdata('openapi_types' => {});
__PACKAGE__->mk_classdata('method_documentation' => {}); 
__PACKAGE__->mk_classdata('class_documentation' => {});

# new plain object
sub new { 
    my ($class, %args) = @_; 

    my $self = bless {}, $class;

    $self->init(%args);
    
    return $self;
}

# initialize the object
sub init
{
    my ($self, %args) = @_;

    foreach my $attribute (keys %{$self->attribute_map}) {
        my $args_key = $self->attribute_map->{$attribute};
        $self->$attribute( $args{ $args_key } );
    }
}

# return perl hash
sub to_hash {
    my $self = shift;
    my $_hash = decode_json(JSON->new->convert_blessed->encode($self));

    return $_hash;
}

# used by JSON for serialization
sub TO_JSON { 
    my $self = shift;
    my $_data = {};
    foreach my $_key (keys %{$self->attribute_map}) {
        if (defined $self->{$_key}) {
            $_data->{$self->attribute_map->{$_key}} = $self->{$_key};
        }
    }

    return $_data;
}

# from Perl hashref
sub from_hash {
    my ($self, $hash) = @_;

    # loop through attributes and use openapi_types to deserialize the data
    while ( my ($_key, $_type) = each %{$self->openapi_types} ) {
        my $_json_attribute = $self->attribute_map->{$_key}; 
        if ($_type =~ /^array\[(.+)\]$/i) { # array
            my $_subclass = $1;
            my @_array = ();
            foreach my $_element (@{$hash->{$_json_attribute}}) {
                push @_array, $self->_deserialize($_subclass, $_element);
            }
            $self->{$_key} = \@_array;
        } elsif ($_type =~ /^hash\[string,(.+)\]$/i) { # hash
            my $_subclass = $1;
            my %_hash = ();
            while (my($_key, $_element) = each %{$hash->{$_json_attribute}}) {
                $_hash{$_key} = $self->_deserialize($_subclass, $_element);
            }
            $self->{$_key} = \%_hash;
        } elsif (exists $hash->{$_json_attribute}) { #hash(model), primitive, datetime
            $self->{$_key} = $self->_deserialize($_type, $hash->{$_json_attribute});
        } else {
            $log->debugf("Warning: %s (%s) does not exist in input hash\n", $_key, $_json_attribute);
        }
    }
  
    return $self;
}

# deserialize non-array data
sub _deserialize {
    my ($self, $type, $data) = @_;
    $log->debugf("deserializing %s with %s",Dumper($data), $type);

    if ($type eq 'DateTime') {
        return DateTime->from_epoch(epoch => str2time($data));
    } elsif ( grep( /^$type$/, ('int', 'double', 'string', 'boolean'))) {
        return $data;
    } else { # hash(model)
        my $_instance = eval "WWW::OpenAPIClient::Object::$type->new()";
        return $_instance->from_hash($data);
    }
}



__PACKAGE__->class_documentation({description => 'Information on matched sensitive data',
                                  class => 'DLPResponseDlpInfo',
                                  required => [], # TODO
}                                 );

__PACKAGE__->method_documentation({
    'certainty' => {
        datatype => 'string',
        base_name => 'certainty',
        description => 'Describes how certain the hit is, possible values:   * &#x60;Very Low&#x60;   * &#x60;Low&#x60;   * &#x60;Medium&#x60;   * &#x60;High&#x60;   * &#x60;Very High&#x60; ',
        format => '',
        read_only => '',
            },
    'errors' => {
        datatype => 'object',
        base_name => 'errors',
        description => 'A  list of error objects (empty if no errors happened), each error object contains following keys:   * &#x60;scan&#x60;: scan related error description   * &#x60;redact&#x60;: redaction related error description   * &#x60;watermark&#x60;: watermark related error description   * &#x60;metadata_removal&#x60;: metadata removal related error description ',
        format => '',
        read_only => '',
            },
    'filename' => {
        datatype => 'string',
        base_name => 'filename',
        description => 'Output processed file name (pre-configured on engine settings under Core&#39;s worflow rule)',
        format => '',
        read_only => '',
            },
    'hits' => {
        datatype => 'DLPResponseDlpInfoHits',
        base_name => 'hits',
        description => '',
        format => '',
        read_only => '',
            },
    'metadata_removal' => {
        datatype => 'DLPResponseDlpInfoMetadataRemoval',
        base_name => 'metadata_removal',
        description => '',
        format => '',
        read_only => '',
            },
    'redact' => {
        datatype => 'DLPResponseDlpInfoRedact',
        base_name => 'redact',
        description => '',
        format => '',
        read_only => '',
            },
    'severity' => {
        datatype => 'int',
        base_name => 'severity',
        description => '(NOTE: this field is deprecated): represents the severity of the data loss, possible values:   * &#x60;0&#x60; - Certainly is data loss   * &#x60;1&#x60; - Might be data loss ',
        format => '',
        read_only => '',
            },
    'verdict' => {
        datatype => 'int',
        base_name => 'verdict',
        description => 'The overall result for the scanned file. It can be   | index         | status                       |   |---------------|------------------------------|   | 0             | Clean                        |   | 1             | Found matched data           |   | 2             | Suspicious                   |   | 3             | Failed                       |   | 4             | Not scanned                  | ',
        format => '',
        read_only => '',
            },
    'watermark' => {
        datatype => 'DLPResponseDlpInfoWatermark',
        base_name => 'watermark',
        description => '',
        format => '',
        read_only => '',
            },
});

__PACKAGE__->openapi_types( {
    'certainty' => 'string',
    'errors' => 'object',
    'filename' => 'string',
    'hits' => 'DLPResponseDlpInfoHits',
    'metadata_removal' => 'DLPResponseDlpInfoMetadataRemoval',
    'redact' => 'DLPResponseDlpInfoRedact',
    'severity' => 'int',
    'verdict' => 'int',
    'watermark' => 'DLPResponseDlpInfoWatermark'
} );

__PACKAGE__->attribute_map( {
    'certainty' => 'certainty',
    'errors' => 'errors',
    'filename' => 'filename',
    'hits' => 'hits',
    'metadata_removal' => 'metadata_removal',
    'redact' => 'redact',
    'severity' => 'severity',
    'verdict' => 'verdict',
    'watermark' => 'watermark'
} );

__PACKAGE__->mk_accessors(keys %{__PACKAGE__->attribute_map});


1;
