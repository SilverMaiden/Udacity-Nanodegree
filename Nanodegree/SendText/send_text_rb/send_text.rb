require 'twilio-ruby'
account_sid = "AC33edeaa4117e4f98a6312624f08b83fa"
auth_token = "2b14f31754460de9d8043356030ab517"
@client = Twilio::REST::Client.new account_sid, auth_token
message = @client.account.messages.create(:body => "Hello from Ruby",
  :to => "+13108040680",
  :from => "+14153648157")

puts message.sid