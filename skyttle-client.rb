require 'rubygems'
require 'rest_client'

values = {
     "text" => "We have visited this restaurant a few times in the past, and the meals have been ok, but this time we were deeply disappointed.",
     "lang" => "en",
     "keywords" => 1,
     "sentiment" => 1,
     "annotate"=> 0
}

headers  = {
     "content_type" => "application/json; charset=utf_8",
     "X-Mashape-Authorization" => YOUR_MASHAPE_KEY
}

response = RestClient.post "https://sentinelprojects-skyttle20.p.mashape.com/", values, headers

puts response
