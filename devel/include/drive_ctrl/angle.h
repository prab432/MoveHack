// Generated by gencpp from file drive_ctrl/angle.msg
// DO NOT EDIT!


#ifndef DRIVE_CTRL_MESSAGE_ANGLE_H
#define DRIVE_CTRL_MESSAGE_ANGLE_H

#include <ros/service_traits.h>


#include <drive_ctrl/angleRequest.h>
#include <drive_ctrl/angleResponse.h>


namespace drive_ctrl
{

struct angle
{

typedef angleRequest Request;
typedef angleResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct angle
} // namespace drive_ctrl


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::drive_ctrl::angle > {
  static const char* value()
  {
    return "f722b4fcc5489fb64570f8162eaa2eed";
  }

  static const char* value(const ::drive_ctrl::angle&) { return value(); }
};

template<>
struct DataType< ::drive_ctrl::angle > {
  static const char* value()
  {
    return "drive_ctrl/angle";
  }

  static const char* value(const ::drive_ctrl::angle&) { return value(); }
};


// service_traits::MD5Sum< ::drive_ctrl::angleRequest> should match 
// service_traits::MD5Sum< ::drive_ctrl::angle > 
template<>
struct MD5Sum< ::drive_ctrl::angleRequest>
{
  static const char* value()
  {
    return MD5Sum< ::drive_ctrl::angle >::value();
  }
  static const char* value(const ::drive_ctrl::angleRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::drive_ctrl::angleRequest> should match 
// service_traits::DataType< ::drive_ctrl::angle > 
template<>
struct DataType< ::drive_ctrl::angleRequest>
{
  static const char* value()
  {
    return DataType< ::drive_ctrl::angle >::value();
  }
  static const char* value(const ::drive_ctrl::angleRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::drive_ctrl::angleResponse> should match 
// service_traits::MD5Sum< ::drive_ctrl::angle > 
template<>
struct MD5Sum< ::drive_ctrl::angleResponse>
{
  static const char* value()
  {
    return MD5Sum< ::drive_ctrl::angle >::value();
  }
  static const char* value(const ::drive_ctrl::angleResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::drive_ctrl::angleResponse> should match 
// service_traits::DataType< ::drive_ctrl::angle > 
template<>
struct DataType< ::drive_ctrl::angleResponse>
{
  static const char* value()
  {
    return DataType< ::drive_ctrl::angle >::value();
  }
  static const char* value(const ::drive_ctrl::angleResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // DRIVE_CTRL_MESSAGE_ANGLE_H