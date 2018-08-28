// Generated by gencpp from file drive_ctrl/angleRequest.msg
// DO NOT EDIT!


#ifndef DRIVE_CTRL_MESSAGE_ANGLEREQUEST_H
#define DRIVE_CTRL_MESSAGE_ANGLEREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace drive_ctrl
{
template <class ContainerAllocator>
struct angleRequest_
{
  typedef angleRequest_<ContainerAllocator> Type;

  angleRequest_()
    : yaw(0)
    , direc(0)  {
    }
  angleRequest_(const ContainerAllocator& _alloc)
    : yaw(0)
    , direc(0)  {
  (void)_alloc;
    }



   typedef int16_t _yaw_type;
  _yaw_type yaw;

   typedef int16_t _direc_type;
  _direc_type direc;




  typedef boost::shared_ptr< ::drive_ctrl::angleRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::drive_ctrl::angleRequest_<ContainerAllocator> const> ConstPtr;

}; // struct angleRequest_

typedef ::drive_ctrl::angleRequest_<std::allocator<void> > angleRequest;

typedef boost::shared_ptr< ::drive_ctrl::angleRequest > angleRequestPtr;
typedef boost::shared_ptr< ::drive_ctrl::angleRequest const> angleRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::drive_ctrl::angleRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::drive_ctrl::angleRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace drive_ctrl

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::drive_ctrl::angleRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::drive_ctrl::angleRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::drive_ctrl::angleRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::drive_ctrl::angleRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::drive_ctrl::angleRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::drive_ctrl::angleRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::drive_ctrl::angleRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "b4d8fe01f1e48843b1e6cb442c7c2186";
  }

  static const char* value(const ::drive_ctrl::angleRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xb4d8fe01f1e48843ULL;
  static const uint64_t static_value2 = 0xb1e6cb442c7c2186ULL;
};

template<class ContainerAllocator>
struct DataType< ::drive_ctrl::angleRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "drive_ctrl/angleRequest";
  }

  static const char* value(const ::drive_ctrl::angleRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::drive_ctrl::angleRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int16 yaw\n\
int16 direc\n\
";
  }

  static const char* value(const ::drive_ctrl::angleRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::drive_ctrl::angleRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.yaw);
      stream.next(m.direc);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct angleRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::drive_ctrl::angleRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::drive_ctrl::angleRequest_<ContainerAllocator>& v)
  {
    s << indent << "yaw: ";
    Printer<int16_t>::stream(s, indent + "  ", v.yaw);
    s << indent << "direc: ";
    Printer<int16_t>::stream(s, indent + "  ", v.direc);
  }
};

} // namespace message_operations
} // namespace ros

#endif // DRIVE_CTRL_MESSAGE_ANGLEREQUEST_H