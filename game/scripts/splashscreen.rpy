image learn_to_code_splash = 'images/others/learnToCodeRPG.png'
image fcc_splash = 'images/others/fcc_primary_large.jpg'

label splashscreen:
    scene gray90 with Pause(1)
    show learn_to_code_splash at truecenter with dissolve
    with Pause(2)
    scene gray90 with dissolve
    with Pause(1)

    scene gray90 with Pause(1)
    show fcc_splash at truecenter with dissolve
    with Pause(2)
    scene gray90 with dissolve
    with Pause(1)
    # return control to the `start` label

    return