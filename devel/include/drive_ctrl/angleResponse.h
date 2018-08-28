// Generated by gencpp from file drive_ctrl/angleResponse.msg
// DO NOT EDIT!


#ifndef DRIVE_CTRL_MESSAGE_ANGLERESPONSE_H
#define DRIVE_CTRL_MESSAGE_ANGLERESPONSE_H


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
struct angleResponse_
{
  typedef angleResponse_<ContainerAllocator> Type;

  angleResponse_()
    : output(false)  {
    }
  angleResponse_(const ContainerAllocator& _alloc)
    : output(false)  {
  (void)_alloc;
    }



   typedef uint8_t _output_type;
  _output_type output;




  typedef boost::shared_ptr< ::drive_ctrl::angleResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::drive_ctrl::angleResponse_<ContainerAllocator> const> ConstPtr;

}; // struct angleResponse_

typedef ::drive_ctrl::angleResponse_<std::allocator<void> > angleResponse;

typedef boost::shared_ptr< ::drive_ctrl::angleResponse > angleResponsePtr;
typedef boost::shared_ptr< ::drive_ctrl::angleResponse const> angleResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::drive_ctrl::angleResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::drive_ctrl::angleResponse_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::drive_ctrl::angleResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::drive_ctrl::angleResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::drive_ctrl::angleResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::drive_ctrl::angleResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::drive_ctrl::angleResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::drive_ctrl::angleResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::drive_ctrl::angleResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d5fa62db5c86ed745052c3b25d12f430";
  }

  static const char* value(const ::drive_ctrl::angleResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd5fa62db5c86ed74ULL;
  static const uint64_t static_value2 = 0x5052c3b25d12f430ULL;
};

template<class ContainerAllocator>
struct DataType< ::drive_ctrl::angleResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "drive_ctrl/angleResponse";
  }

  static const char* value(const ::drive_ctrl::angleResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::drive_ctrl::angleResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool output\n\
\n\
";
  }

  static const char* value(const ::drive_ctrl::angleResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::drive_ctrl::angleResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.output);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct angleResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::drive_ctrl::angleResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::drive_ctrl::angleResponse_<ContainerAllocator>& v)
  {
    s << indent << "output: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.output);
  }
};

} // namespace message_operations
} // namespace ros

#endif // DRIVE_CTRL_MESSAGE_ANGLERESPONSE_H
