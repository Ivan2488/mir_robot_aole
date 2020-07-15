#!/usr/bin/env python


import communic 
import rospy



mov = communic.movement()

rate = rospy.Rate(4)

while not rospy.is_shutdown() :

	
	"""mov.move_forward()
	mov.publish_vel()
        rate.sleep()

	mov.move_forward()
	mov.publish_vel()
        rate.sleep()"""

	mov.rotate_left()
	mov.publish_vel()
        rate.sleep()

	"""mov.move_forward()
	mov.publish_vel()
        rate.sleep()

	mov.move_forward()
	mov.publish_vel()
        rate.sleep()

	mov.rotate_left()
	mov.publish_vel()
        rate.sleep()

	mov.move_forward()
	mov.publish_vel()
        rate.sleep()

	mov.move_forward()
	mov.publish_vel()
        rate.sleep()

	mov.rotate_left()
	mov.publish_vel()
        rate.sleep()

	mov.move_forward()
	mov.publish_vel()
        rate.sleep()

	mov.move_forward()
	mov.publish_vel()
        rate.sleep()

	mov.rotate_left()
	mov.publish_vel()
        rate.sleep()"""

        """movement = raw_input('Enter desired movement: ')

        if movement == 'forward':
            mov.move_forward()

        if movement == 'backward':
            mov.move_backward()

        if movement == 'stop':
            mov.stop()"""

        
