# snake_panel
PyQt based control panel for the locomotion of snake robot.

ROS topic message type, __/gait_param__ has 6 elements:
- /amp : float32, range 0~20
- /freq : float32, range 0~2.0
- /hor_amp : float32, range 0~20
- /nu : float32, range 0~0.2
- /phi : float32
- /gait : string, | Rollinng | Sidewinding | Vertical | Pipe-Crawling | Sinuslifting | Rotating |

<center><img src="https://github.com/SeunghyunLim/snake_panel/blob/main/gif/panel_topic.gif" alt="drawing" width="720"/></center>
<center><img src="https://github.com/SeunghyunLim/snake_panel/blob/main/gif/panel_control.gif" alt="drawing" width="720"/></center>
<center><img src="https://github.com/SeunghyunLim/snake_panel/blob/main/gif/panel_rolling.gif" alt="drawing" width="720"/></center>


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
