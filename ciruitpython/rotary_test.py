import board
import digitalio

# The logic of the rotary dial is a little confusing at first, but the way it works is each "step" of the rotation
# alternates between True and False. Becuase there are two sensors the main sensor (pin GP16 in this example)
# when that changes from True to False, or False to True we check the secondary sensor (pin GP17 in this example.)
# If that secondary sensor is True then we know it rotated in one direction, if its reading false we know it turned
# the other way. We can use this though a series of "if" statements to figure out what direction we are turning.


# define the drive and step as two seperate switches
rotate_drive = digitalio.DigitalInOut(board.GP16)
rotate_drive.direction = digitalio.Direction.INPUT
rotate_drive.pull = digitalio.Pull.UP

rotate_step = digitalio.DigitalInOut(board.GP17)
rotate_step.direction = digitalio.Direction.INPUT
rotate_step.pull = digitalio.Pull.UP

# set the default positon to None so we have a starting value we can do special things with if desired
last_position = None

# starts the count at 0, can be changed to whatever the starting value should be.
count = 0


while True:
    position = rotate_drive.value
    direction = rotate_step.value
    if last_position is None or position != last_position:
        # When the script first runs this block will run, so can set any startup actions to occur here
        if last_position is None:
            print("Initial setup")
            last_position = position
        # if the position is True this block will run, which is every other position of the dial
        elif position:
            # if the direction is False then the dial was rotated clockwise
            if direction is not True:
                count += 1
                print(f"turned clockwise, count {count}")
                last_position = position
            # if the direction is true then the dial was rotated anticlockwise.
            else:
                count -= 1
                print(f"turned anticlockwise, count {count}")
                last_position = position
        # if the position is False then this block will run, which is every other position of the dial
        elif not position:
            # If direction is true then the dial was turned clockwise (the reverse of the previous block)
            if direction is True:
                count += 1
                print(f"turned clockwise, count {count}")
                last_position = position
            # If the direction is False then the dial was turned anticlockwise (the reverse of the previous block)
            else:
                count -= 1
                print(f"turned anticlockwise, count {count}")
                last_position = position
        
        
        