from plyer import notification

notification.notify(
    title="Better Python Project",
    message="Here is your notification body",
    app_icon="logo.ico",  # 可选参数
    timeout=10  # 持续时间（秒）
)
