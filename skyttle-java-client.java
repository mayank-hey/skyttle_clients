import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;

public class Client {

	public static void main(String[] args) throws UnsupportedEncodingException{
		String url = "http://livenlp.aws.af.cm/v0.1/";
		String text = "The car is underpowered and often loses traction.";
		String username = "<your username>";
		String pwd = "<your password>";
		String lang = "en";
		String domain = "automotive";
		String keywords = "1";
		String sentiment = "1";
		String annotate = "1";

		String params =
		        "text=" + URLEncoder.encode(text, "UTF-8") +
		        "&user=" + URLEncoder.encode(username, "UTF-8") +
		        "&pwd=" + URLEncoder.encode(password, "UTF-8") +
		        "&lang=" + URLEncoder.encode(lang, "UTF-8") +
		        "&keywords=" + URLEncoder.encode(keywords, "UTF-8") +
		        "&sentiment=" + URLEncoder.encode(sentiment, "UTF-8") +
		        "&annotate=" + URLEncoder.encode(annotate, "UTF-8");

		String response = makeCall(url, params);
		System.out.println("Response: " + response);

	}

	public static String makeCall(String targetURL, String urlParameters)
	  {
	    URL url;
	    HttpURLConnection connection = null;
	    try {
	      // create connection
	      url = new URL(targetURL);
	      connection = (HttpURLConnection) url.openConnection();
	      connection.setRequestMethod("POST");
	      connection.setRequestProperty("Content-Type",
	      				"application/x-www-form-urlencoded");
	      connection.setUseCaches (false);
	      connection.setDoInput(true);
	      connection.setDoOutput(true);

	      // send request
	      DataOutputStream wr = new DataOutputStream (
	                  connection.getOutputStream ());
	      wr.writeBytes(urlParameters);
	      wr.flush();
	      wr.close();

	      // get Response
	      InputStream is = connection.getInputStream();
	      BufferedReader rd = new BufferedReader(new InputStreamReader(is));
	      String line;
	      StringBuffer response = new StringBuffer();
	      while((line = rd.readLine()) != null) {
	        response.append(line);
	        response.append('\r');
	      }
	      rd.close();
	      return response.toString();

	    } catch (Exception e) {

	      e.printStackTrace();
	      return null;

	    } finally {

	      if(connection != null) {
	        connection.disconnect();
	      }
	    }
	  }

}