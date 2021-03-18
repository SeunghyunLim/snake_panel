# snake_panel
PyQt based control panel for the locomotion of snake robot.

ROS topic message type, __/gait_param__ has 6 elements: 
- /amp : float32
- /freq : float32
- /hor_amp : float32
- /nu : float32
- /phi : float32
- /gait : string

<center><img src="https://github.com/SeunghyunLim/snake_panel/blob/main/gif/panel_topic.gif" alt="drawing" width="720"/></center>


## Rolling gait
- Amplitude
- Frequency

## Pipe-Crawling gait
- Amplitude
- Phi
- Nu
- Frequency

## Sidewinding gait
- Amplitude
- Frequency

## Verticalsine gait
- Amplitude
- Frequency

## Rotating gait
- Vertical Amplitude
- Horizontal Amplitude
- Frequency

## Sinuslifting gait
- Vertical Amplitude
- Horizontal Amplitude
- Frequency
