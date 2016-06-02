function drawPcapChart(pcap_json_label,pcap_json_obj) {
	ctx = document.getElementById("chartarea");
	var chartarea = new Chart(ctx, {
		type: "scatter",
		data: {
			datasets: [
				{
					label: pcap_json_label,
					data: pcap_json_obj,
					lineTension: 0,
				}
			],
		},
	});
};
