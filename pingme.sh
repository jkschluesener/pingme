# pingme.sh

# A simple bash script to send a telegram message to yourself.

# Usage:
# $ pingme message_text api_key chatid disable_notification
# Example:
# $ pingme ImportantMessage <secretkey> <chatid> true
# The message can be markdown formatted, in that case add quotation marks
# $ pingme "Important Message: Submitted job *crashed*!" <secretkey> <chatid> false
# For easier usage, set the api key and chatid based on your need within the function.
# Or better yet, grab the keys from the env.

# Installation:
# Drop this file in your working directory.
# Or into your bash script (e.g. slurm / moab submission script)
# Or append this scripts path to your system PATH.

# For a guide on how to setup your telegram bot, see README.md

# Confirmed to work on Linux and Mac.

# Note on the API key:
# Keys seem to contain a `:`, replace with `%`

# Jan K. Schluesener
# github.com/jkschluesener/pingme
# MIT License

pingme() {

  text=$1
  apikey=$2
  chatid=$3
  disable_notification=$4

  curl --request POST \
      --url https://api.telegram.org/bot$apikey/sendMessage \
      --header 'accept: application/json' \
      --header 'content-type: application/json' \
      --data "
              {
                  \"text\": \"$text\",
                  \"parse_mode\": \"markdown\",
                  \"disable_web_page_preview\": true,
                  \"disable_notification\": \"$disable_notification\",
                  \"reply_to_message_id\": null,
                  \"chat_id\": \"$chatid\"
              }
              "
}
