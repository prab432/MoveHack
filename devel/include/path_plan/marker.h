// Generated by gencpp from file path_plan/marker.msg
// DO NOT EDIT!


#ifndef PATH_PLAN_MESSAGE_MARKER_H
#define PATH_PLAN_MESSAGE_MARKER_H

#include <ros/service_traits.h>


#include <path_plan/markerRequest.h>
#include <path_plan/markerResponse.h>


namespace path_plan
{

struct marker
{

typedef markerRequest Request;
typedef markerResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct marker
} // namespace path_plan


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::path_plan::marker > {
  static const char* value()
  {
    return "8647635e75097d7d18330a4887453582";
  }

  static const char* value(const ::path_plan::marker&) { return value(); }
};

template<>
struct DataType< ::path_plan::marker > {
  static const char* value()
  {
    return "path_plan/marker";
  }

  static const char* value(const ::path_plan::marker&) { return value(); }
};


// service_traits::MD5Sum< ::path_plan::markerRequest> should match 
// service_traits::MD5Sum< ::path_plan::marker > 
template<>
struct MD5Sum< ::path_plan::markerRequest>
{
  static const char* value()
  {
    return MD5Sum< ::path_plan::marker >::value();
  }
  static const char* value(const ::path_plan::markerRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::path_plan::markerRequest> should match 
// service_traits::DataType< ::path_plan::marker > 
template<>
struct DataType< ::path_plan::markerRequest>
{
  static const char* value()
  {
    return DataType< ::path_plan::marker >::value();
  }
  static const char* value(const ::path_plan::markerRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::path_plan::markerResponse> should match 
// service_traits::MD5Sum< ::path_plan::marker > 
template<>
struct MD5Sum< ::path_plan::markerResponse>
{
  static const char* value()
  {
    return MD5Sum< ::path_plan::marker >::value();
  }
  static const char* value(const ::path_plan::markerResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::path_plan::markerResponse> should match 
// service_traits::DataType< ::path_plan::marker > 
template<>
struct DataType< ::path_plan::markerResponse>
{
  static const char* value()
  {
    return DataType< ::path_plan::marker >::value();
  }
  static const char* value(const ::path_plan::markerResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // PATH_PLAN_MESSAGE_MARKER_H