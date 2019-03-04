while :
do
	mosquitto_pub -h 192.168.40.222 -t "test" -m "Good Papi" -u "admin" -P "password"
	sleep 5
done

