import boto3
import os

# create cloudwatch client
cloudwatch = boto3.client('cloudwatch')
# create sns client
sns_client = boto3.client('sns')

def lambda_handler(event, context):
        # Take only specific alarms to disable, provide alarms w/out spaces i.e alarm1,alarm2,alarmn
        # Initialize alarms list parameter
        ALARMS = []
        ALARMS = os.environ['ALARMS']
        ALARMS = ALARMS.split(",")
        for alarmname in ALARMS:
            cloudwatch.enable_alarm_actions(AlarmNames=[alarmname])
            print("Alarm: " + alarmname + " has been enabled!")
        #Send SNS msg
        response = sns_client.publish(
                TopicArn = os.environ['SNS_TOPIC_ARN'],
                Message = os.environ['ALARMS'],
                Subject = "Alarm Enabled"
                )
