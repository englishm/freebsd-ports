--- grc/gen_osmosdr_blocks.py.orig	2018-08-15 17:53:26 UTC
+++ grc/gen_osmosdr_blocks.py
@@ -19,478 +19,388 @@ Foundation, Inc., 51 Franklin Street, Fifth Floor, Bos
 """
 
 MAIN_TMPL = """\
-<?xml version="1.0"?>
-<block>
-  <name>$(title) $sourk.title()</name>
-  <key>$(prefix)_$(sourk)</key>
-  <category>$($sourk.title())s</category>
-  <throttle>1</throttle>
-  <import>import osmosdr</import>
-  <import>import time</import>
-  <make>osmosdr.$(sourk)( args="numchan=" + str(\$nchan) + " " + \$args )
-#for $m in range($max_mboards)
-########################################################################
-\#if \$num_mboards() > $m and \$clock_source$(m)()
-self.\$(id).set_clock_source(\$clock_source$(m), $m)
-\#end if
-########################################################################
-\#if \$num_mboards() > $m and \$time_source$(m)()
-self.\$(id).set_time_source(\$time_source$(m), $m)
-\#end if
-########################################################################
-#end for
-\#if \$sync() == 'sync'
-self.\$(id).set_time_unknown_pps(osmosdr.time_spec_t())
-\#elif \$sync() == 'pc_clock'
-self.\$(id).set_time_now(osmosdr.time_spec_t(time.time()), osmosdr.ALL_MBOARDS)
-\#end if
-self.\$(id).set_sample_rate(\$sample_rate)
-#for $n in range($max_nchan)
-\#if \$nchan() > $n
-self.\$(id).set_center_freq(\$freq$(n), $n)
-self.\$(id).set_freq_corr(\$corr$(n), $n)
-#if $sourk == 'source':
-self.\$(id).set_dc_offset_mode(\$dc_offset_mode$(n), $n)
-self.\$(id).set_iq_balance_mode(\$iq_balance_mode$(n), $n)
-self.\$(id).set_gain_mode(\$gain_mode$(n), $n)
-#end if
-self.\$(id).set_gain(\$gain$(n), $n)
-self.\$(id).set_if_gain(\$if_gain$(n), $n)
-self.\$(id).set_bb_gain(\$bb_gain$(n), $n)
-self.\$(id).set_antenna(\$ant$(n), $n)
-self.\$(id).set_bandwidth(\$bw$(n), $n)
-\#end if
-#end for
-  </make>
-  <callback>set_sample_rate(\$sample_rate)</callback>
-  #for $n in range($max_nchan)
-  <callback>set_center_freq(\$freq$(n), $n)</callback>
-  <callback>set_freq_corr(\$corr$(n), $n)</callback>
-  #if $sourk == 'source':
-  <callback>set_dc_offset_mode(\$dc_offset_mode$(n), $n)</callback>
-  <callback>set_iq_balance_mode(\$iq_balance_mode$(n), $n)</callback>
-  <callback>set_gain_mode(\$gain_mode$(n), $n)</callback>
-  #end if
-  <callback>set_gain(\$gain$(n), $n)</callback>
-  <callback>set_if_gain(\$if_gain$(n), $n)</callback>
-  <callback>set_bb_gain(\$bb_gain$(n), $n)</callback>
-  <callback>set_antenna(\$ant$(n), $n)</callback>
-  <callback>set_bandwidth(\$bw$(n), $n)</callback>
-  #end for
-  <param>
-    <name>$(dir.title())put Type</name>
-    <key>type</key>
-    <type>enum</type>
-    <option>
-      <name>Complex float32</name>
-      <key>fc32</key>
-      <opt>type:fc32</opt>
-    </option>
-  </param>
-  <param>
-    <name>Device Arguments</name>
-    <key>args</key>
-    <value></value>
-    <type>string</type>
-    <hide>
-      \#if \$args()
-        none
-      \#else
-        part
-      \#end if
-    </hide>
-  </param>
-  <param>
-    <name>Sync</name>
-    <key>sync</key>
-    <value></value>
-    <type>enum</type>
-    <hide>\#if \$sync() then 'none' else 'part'#</hide>
-    <option>
-      <name>unknown PPS</name>
-      <key>sync</key>
-    </option>
-    <option>
-      <name>PC Clock</name>
-      <key>pc_clock</key>
-    </option>
-    <option>
-      <name>don't sync</name>
-      <key></key>
-    </option>
-  </param>
-  <param>
-    <name>Num Mboards</name>
-    <key>num_mboards</key>
-    <value>1</value>
-    <type>int</type>
-    <hide>part</hide>
-    #for $m in range(1, $max_mboards+1)
-    <option>
-      <name>$(m)</name>
-      <key>$m</key>
-    </option>
-    #end for
-  </param>
-  #for $m in range($max_mboards)
-  <param>
-    <name>Mb$(m): Clock Source</name>
-    <key>clock_source$(m)</key>
-    <value></value>
-    <type>string</type>
-    <hide>
-      \#if not \$num_mboards() > $m
-        all
-      \#elif \$clock_source$(m)()
-        none
-      \#else
-        part
-      \#end if
-    </hide>
-    <option><name>Default</name><key></key></option>
-    <option><name>Internal</name><key>internal</key></option>
-    <option><name>External</name><key>external</key></option>
-    <option><name>External 1PPS</name><key>external_1pps</key></option>
-    <option><name>MIMO Cable</name><key>mimo</key></option>
-    <option><name>O/B GPSDO</name><key>gpsdo</key></option>
-  </param>
-  <param>
-    <name>Mb$(m): Time Source</name>
-    <key>time_source$(m)</key>
-    <value></value>
-    <type>string</type>
-    <hide>
-      \#if not \$num_mboards() > $m
-        all
-      \#elif \$time_source$(m)()
-        none
-      \#else
-        part
-      \#end if
-    </hide>
-    <option><name>Default</name><key></key></option>
-    <option><name>External</name><key>external</key></option>
-    <option><name>MIMO Cable</name><key>mimo</key></option>
-    <option><name>O/B GPSDO</name><key>gpsdo</key></option>
-  </param>
-  #end for
-  <param>
-    <name>Num Channels</name>
-    <key>nchan</key>
-    <value>1</value>
-    <type>int</type>
-    #for $n in range(1, $max_nchan+1)
-    <option>
-      <name>$(n)</name>
-      <key>$n</key>
-    </option>
-    #end for
-  </param>
-  <param>
-    <name>Sample Rate (sps)</name>
-    <key>sample_rate</key>
-    <value>samp_rate</value>
-    <type>real</type>
-  </param>
-  $params
-  <check>$max_nchan >= \$nchan</check>
-  <check>\$nchan > 0</check>
-  <check>$max_mboards >= \$num_mboards</check>
-  <check>\$num_mboards > 0</check>
-  <check>\$nchan >= \$num_mboards</check>
-  <$sourk>
-    <name>$dir</name>
-    <type>\$type.type</type>
-    <nports>\$nchan</nports>
-  </$sourk>
-  <doc>
-The osmocom $sourk block:
+id: ${prefix}_${sourk}
+label: '${title} ${sourk.title()}'
+category: '[OsmoSDR]'
+flags: throttle
 
-While primarily being developed for the OsmoSDR hardware, this block as well supports:
+parameters:
+- id: type
+  label: '${direction.title()}put Type'
+  dtype: enum
+  options: [fc32]
+  option_labels: [Complex Float32]
+  option_attributes:
+      type: [fc32]
+  hide: part
+- id: args
+  label: 'Device Arguments'
+  dtype: string
+  default: '""'
+  hide: ${'$'}{ 'none' if args else 'part'}
+- id: sync
+  label: Sync
+  dtype: enum
+  options: [sync, pc_clock, none]
+  option_labels: [Unknown PPS, PC Clock, Don't Sync]
+  hide: ${'$'}{ 'none' if sync else 'part'}
+- id: num_mboards
+  label: 'Number MBoards'
+  dtype: int
+  default: 1
+  options: [ ${", ".join([str(n) for n in range(1, max_mboards+1)])} ]
+  hide: part
+% for m in range(max_mboards):
+- id: clock_source${m}
+  label: 'MB${m}: Clock Source'
+  dtype: string
+  options: ['', internal, external, external_1pps, mimo, gpsdo]
+  option_labels: [Default, Internal, External, External 1PPS, MIMO Cable, O/B GPSDO]
+  hide: ${'$'}{ 'all' if not (num_mboards > ${m}) else ( 'none' if clock_source${m} else 'part' )}
+- id: time_source${m}
+  label: 'MB${m}: Time Source'
+  dtype: string
+  options: ['', external, mimo, gpsdo]
+  option_labels: [Default, External, MIMO Cable, O/B GPSDO]
+  hide: ${'$'}{ 'all' if not (num_mboards > ${m}) else ( 'none' if time_source${m} else 'part' )}  
+% endfor
+- id: nchan
+  label: 'Number Channels'
+  dtype: int
+  default: 1
+  options: [ ${", ".join([str(n) for n in range(1, max_nchan+1)])} ]
+- id: sample_rate
+  label: 'Sample Rate (sps)'
+  dtype: real
+  default: samp_rate
+${params}
 
-#if $sourk == 'source':
- * FUNcube Dongle through libgnuradio-fcd
- * FUNcube Dongle Pro+ through gr-fcdproplus
- * sysmocom OsmoSDR Devices through libosmosdr
- * RTL2832U based DVB-T dongles through librtlsdr
- * RTL-TCP spectrum server (see librtlsdr project)
- * MSi2500 based DVB-T dongles through libmirisdr
- * SDRplay RSP devices through SDRplay library
- * gnuradio .cfile input through libgnuradio-blocks
- * RFSPACE SDR-IQ, SDR-IP, NetSDR (incl. X2 option)
- * AirSpy Wideband Receiver through libairspy
-#end if
-#if $sourk == 'sink':
- * gnuradio .cfile output through libgnuradio-blocks
-#end if
- * CCCamp 2015 rad1o Badge through libhackrf
- * Great Scott Gadgets HackRF through libhackrf
- * Nuand LLC bladeRF through libbladeRF library
- * Ettus USRP Devices through Ettus UHD library
- * Fairwaves UmTRX through Fairwaves' fork of UHD
- * Red Pitaya SDR transceiver (http://bazaar.redpitaya.com)
- * FreeSRP through libfreesrp library
+inputs:
+- domain: message
+  id: command
+  optional: true
+% if sourk == 'source':
 
-By using the osmocom $sourk block you can take advantage of a common software api in your application(s) independent of the underlying radio hardware.
+outputs:
+% endif
+- domain: stream
+  dtype: ${'$'}{type.type}
+  multiplicity: ${'$'}{nchan}
+% if sourk == 'sink':
 
-Output Type:
-This parameter controls the data type of the stream in gnuradio. Only complex float32 samples are supported at the moment.
+outputs:
+- domain: message
+  id: async_msgs
+  optional: true
+% endif
 
-Device Arguments:
-The device argument is a comma delimited string used to locate devices on your system. Device arguments for multiple devices may be given by separating them with a space.
-Use the device id or name/serial (if applicable) to specify a certain device or list of devices. If left blank, the first device found will be used.
+templates:
+  imports: |-
+     import osmosdr
+     import time
+  make: |
+    osmosdr.${sourk}(
+        args="numchan=" + str(${'$'}{nchan}) + " " + ${'$'}{args}
+    )
+    % for m in range(max_mboards):
+    ${'%'} if context.get('num_mboards')() > ${m}:
+    ${'%'} if context.get('clock_source${m}')():
+    self.${'$'}{id}.set_clock_source(${'$'}{${'clock_source' + str(m)}}, ${m})
+    ${'%'} endif
+    ${'%'} if context.get('time_source${m}')():
+    self.${'$'}{id}.set_time_source(${'$'}{${'time_source' + str(m)}}, ${m})
+    ${'%'} endif
+    ${'%'} endif
+    % endfor
+    ${'%'} if sync == 'sync':
+    self.${'$'}{id}.set_time_unknown_pps(osmosdr.time_spec_t())
+    ${'%'} elif sync == 'pc_clock':
+    self.${'$'}{id}.set_time_now(osmosdr.time_spec_t(time.time()), osmosdr.ALL_MBOARDS)
+    ${'%'} endif
+    self.${'$'}{id}.set_sample_rate(${'$'}{sample_rate})
+    % for n in range(max_nchan):
+    ${'%'} if context.get('nchan')() > ${n}:
+    self.${'$'}{id}.set_center_freq(${'$'}{${'freq' + str(n)}}, ${n})
+    self.${'$'}{id}.set_freq_corr(${'$'}{${'corr' + str(n)}}, ${n})
+    ${'%'} if context.get('sourk') == 'source':
+    self.${'$'}{id}.set_dc_offset_mode(${'$'}{${'dc_offset_mode' + str(n)}}, ${n})
+    self.${'$'}{id}.set_iq_balance_mode(${'$'}{${'iq_balance_mode' + str(n)}}, ${n})
+    self.${'$'}{id}.set_gain_mode(${'$'}{${'gain_mode' + str(n)}}, ${n})
+    ${'%'} endif
+    self.${'$'}{id}.set_gain(${'$'}{${'gain' + str(n)}}, ${n})
+    self.${'$'}{id}.set_if_gain(${'$'}{${'if_gain' + str(n)}}, ${n})
+    self.${'$'}{id}.set_bb_gain(${'$'}{${'bb_gain' + str(n)}}, ${n})
+    self.${'$'}{id}.set_antenna(${'$'}{${'ant' + str(n)}}, ${n})
+    self.${'$'}{id}.set_bandwidth(${'$'}{${'bw' + str(n)}}, ${n})
+    ${'%'} endif
+    % endfor
+  callbacks:
+    - set_sample_rate(${'$'}{sample_rate})
+    % for n in range(max_nchan):
+    - set_center_freq(${'$'}{${'freq' + str(n)}}, ${n})
+    - set_freq_corr(${'$'}{${'corr' + str(n)}}, ${n})
+    % if sourk == 'source':
+    - set_dc_offset_mode(${'$'}{${'dc_offset_mode' + str(n)}}, ${n})
+    - set_iq_balance_mode(${'$'}{${'iq_balance_mode' + str(n)}}, ${n})
+    - set_gain_mode(${'$'}{${'gain_mode' + str(n)}}, ${n})
+    % endif
+    - set_gain(${'$'}{${'gain' + str(n)}}, ${n})
+    - set_if_gain(${'$'}{${'if_gain' + str(n)}}, ${n})
+    - set_bb_gain(${'$'}{${'bb_gain' + str(n)}}, ${n})
+    - set_antenna(${'$'}{${'ant' + str(n)}}, ${n})
+    - set_bandwidth(${'$'}{${'bw' + str(n)}}, ${n})
+    % endfor
 
-Examples:
+documentation: |-
+  The osmocom ${sourk} block:
 
-Optional arguments are placed into [] brackets, remove the brackets before using them! Specific variable values are separated with a |, choose one of them. Variable values containing spaces shall be enclosed in '' as demonstrated in examples section below.
-Lines ending with ... mean it's possible to bind devices together by specifying multiple device arguments separated with a space.
+  While primarily being developed for the OsmoSDR hardware, this block as well supports:
 
-#if $sourk == 'source':
-  fcd=0[,device=hw:2][,type=2]
-  miri=0[,buffers=32] ...
-  rtl=serial_number ...
-  rtl=0[,rtl_xtal=28.8e6][,tuner_xtal=28.8e6] ...
-  rtl=1[,buffers=32][,buflen=N*512] ...
-  rtl=2[,direct_samp=0|1|2][,offset_tune=0|1][,bias=0|1] ...
-  rtl_tcp=127.0.0.1:1234[,psize=16384][,direct_samp=0|1|2][,offset_tune=0|1][,bias=0|1] ...
-  osmosdr=0[,buffers=32][,buflen=N*512] ...
-  file='/path/to/your file',rate=1e6[,freq=100e6][,repeat=true][,throttle=true] ...
-  netsdr=127.0.0.1[:50000][,nchan=2]
-  sdr-ip=127.0.0.1[:50000]
-  cloudiq=127.0.0.1[:50000]
-  sdr-iq=/dev/ttyUSB0
-  airspy=0[,bias=0|1][,linearity][,sensitivity]
-#end if
-#if $sourk == 'sink':
-  file='/path/to/your file',rate=1e6[,freq=100e6][,append=true][,throttle=true] ...
-#end if
-  redpitaya=192.168.1.100[:1001]
-  freesrp=0[,fx3='path/to/fx3.img',fpga='path/to/fpga.bin',loopback]
-  hackrf=0[,buffers=32][,bias=0|1][,bias_tx=0|1]
-  bladerf=0[,tamer=internal|external|external_1pps][,smb=25e6]
-  uhd[,serial=...][,lo_offset=0][,mcr=52e6][,nchan=2][,subdev='\\\\'B:0 A:0\\\\''] ...
+  % if sourk == 'source':
+   * sysmocom OsmoSDR Devices through libosmosdr
+   * RTL2832U based DVB-T dongles through librtlsdr
+   * RTL-TCP spectrum server (see librtlsdr project)
+   * MSi2500 based DVB-T dongles through libmirisdr
+   * SDRplay RSP devices through SDRplay library
+   * gnuradio .cfile input through libgnuradio-blocks
+   * RFSPACE SDR-IQ, SDR-IP, NetSDR (incl. X2 option)
+   * AirSpy Wideband Receiver through libairspy
+  % endif
+  % if sourk == 'sink':
+   * gnuradio .cfile output through libgnuradio-blocks
+  % endif
+   * CCCamp 2015 rad1o Badge through libhackrf
+   * Great Scott Gadgets HackRF through libhackrf
+   * Nuand LLC bladeRF through libbladeRF library
+   * Ettus USRP Devices through Ettus UHD library
+   * Fairwaves UmTRX through Fairwaves' fork of UHD
+   * Red Pitaya SDR transceiver (http://bazaar.redpitaya.com)
+   * FreeSRP through libfreesrp library
 
-Num Channels:
-Selects the total number of channels in this multi-device configuration. Required when specifying multiple device arguments.
+  By using the osmocom $sourk block you can take advantage of a common software api in your application(s) independent of the underlying radio hardware.
 
-Sample Rate:
-The sample rate is the number of samples per second output by this block on each channel.
+  Output Type:
+  This parameter controls the data type of the stream in gnuradio. Only complex float32 samples are supported at the moment.
 
-Frequency:
-The center frequency is the frequency the RF chain is tuned to.
+  Device Arguments:
+  The device argument is a comma delimited string used to locate devices on your system. Device arguments for multiple devices may be given by separating them with a space.
+  Use the device id or name/serial (if applicable) to specify a certain device or list of devices. If left blank, the first device found will be used.
 
-Freq. Corr.:
-The frequency correction factor in parts per million (ppm). Set to 0 if unknown.
+  Examples:
 
-#if $sourk == 'source':
-DC Offset Mode:
-Controls the behavior of hardware DC offset corrrection.
-  Off: Disable correction algorithm (pass through).
-  Manual: Keep last estimated correction when switched from Automatic to Manual.
-  Automatic: Periodicallly find the best solution to compensate for DC offset.
+  Optional arguments are placed into [] brackets, remove the brackets before using them! Specific variable values are separated with a |, choose one of them. Variable values containing spaces shall be enclosed in '' as demonstrated in examples section below.
+  Lines ending with ... mean it's possible to bind devices together by specifying multiple device arguments separated with a space.
 
-This functionality is available for USRP devices only.
+  % if sourk == 'source':
+    miri=0[,buffers=32] ...
+    rtl=serial_number ...
+    rtl=0[,rtl_xtal=28.8e6][,tuner_xtal=28.8e6] ...
+    rtl=1[,buffers=32][,buflen=N*512] ...
+    rtl=2[,direct_samp=0|1|2][,offset_tune=0|1][,bias=0|1] ...
+    rtl_tcp=127.0.0.1:1234[,psize=16384][,direct_samp=0|1|2][,offset_tune=0|1][,bias=0|1] ...
+    osmosdr=0[,buffers=32][,buflen=N*512] ...
+    file='/path/to/your file',rate=1e6[,freq=100e6][,repeat=true][,throttle=true] ...
+    netsdr=127.0.0.1[:50000][,nchan=2]
+    sdr-ip=127.0.0.1[:50000]
+    cloudiq=127.0.0.1[:50000]
+    sdr-iq=/dev/ttyUSB0
+    airspy=0[,bias=0|1][,linearity][,sensitivity]
+  % endif
+  % if sourk == 'sink':
+    file='/path/to/your file',rate=1e6[,freq=100e6][,append=true][,throttle=true] ...
+  % endif
+    redpitaya=192.168.1.100[:1001]
+    freesrp=0[,fx3='path/to/fx3.img',fpga='path/to/fpga.bin',loopback]
+    hackrf=0[,buffers=32][,bias=0|1][,bias_tx=0|1]
+    bladerf=0[,tamer=internal|external|external_1pps][,smb=25e6]
+    uhd[,serial=...][,lo_offset=0][,mcr=52e6][,nchan=2][,subdev='\\\\'B:0 A:0\\\\''] ...
 
-IQ Balance Mode:
-Controls the behavior of software IQ imbalance corrrection.
-  Off: Disable correction algorithm (pass through).
-  Manual: Keep last estimated correction when switched from Automatic to Manual.
-  Automatic: Periodicallly find the best solution to compensate for image signals.
+  Num Channels:
+  Selects the total number of channels in this multi-device configuration. Required when specifying multiple device arguments.
 
-This functionality depends on http://cgit.osmocom.org/cgit/gr-iqbal/
+  Sample Rate:
+  The sample rate is the number of samples per second output by this block on each channel.
 
-Gain Mode:
-Chooses between the manual (default) and automatic gain mode where appropriate.
-To allow manual control of RF/IF/BB gain stages, manual gain mode must be configured.
-Currently, only RTL-SDR devices support automatic gain mode.
+  Frequency:
+  The center frequency is the frequency the RF chain is tuned to.
 
-#end if
-RF Gain:
-Overall RF gain of the device.
+  Freq. Corr.:
+  The frequency correction factor in parts per million (ppm). Set to 0 if unknown.
 
-IF Gain:
-Overall intermediate frequency gain of the device.
-This setting is available for RTL-SDR and OsmoSDR devices with E4000 tuners and HackRF in receive and transmit mode. Observations lead to a reasonable gain range from 15 to 30dB.
+  % if sourk == 'source':
+  DC Offset Mode:
+  Controls the behavior of hardware DC offset corrrection.
+    Off: Disable correction algorithm (pass through).
+    Manual: Keep last estimated correction when switched from Automatic to Manual.
+    Automatic: Periodicallly find the best solution to compensate for DC offset.
 
-BB Gain:
-Overall baseband gain of the device.
-This setting is available for HackRF in receive mode. Observations lead to a reasonable gain range from 15 to 30dB.
+  This functionality is available for USRP devices only.
 
-Antenna:
-For devices with only one antenna, this may be left blank.
-Otherwise, the user should specify one of the possible antenna choices.
+  IQ Balance Mode:
+  Controls the behavior of software IQ imbalance corrrection.
+    Off: Disable correction algorithm (pass through).
+    Manual: Keep last estimated correction when switched from Automatic to Manual.
+    Automatic: Periodicallly find the best solution to compensate for image signals.
 
-Bandwidth:
-Set the bandpass filter on the radio frontend. To use the default (automatic) bandwidth filter setting, this should be zero.
+  This functionality depends on http://cgit.osmocom.org/cgit/gr-iqbal/
 
-See the OsmoSDR project page for more detailed documentation:
-http://sdr.osmocom.org/trac/wiki/GrOsmoSDR
-http://sdr.osmocom.org/trac/wiki/rtl-sdr
-http://sdr.osmocom.org/trac/
-  </doc>
-</block>
+  Gain Mode:
+  Chooses between the manual (default) and automatic gain mode where appropriate.
+  To allow manual control of RF/IF/BB gain stages, manual gain mode must be configured.
+  Currently, only RTL-SDR devices support automatic gain mode.
+
+  % endif
+  RF Gain:
+  Overall RF gain of the device.
+
+  IF Gain:
+  Overall intermediate frequency gain of the device.
+  This setting is available for RTL-SDR and OsmoSDR devices with E4000 tuners and HackRF in receive and transmit mode. Observations lead to a reasonable gain range from 15 to 30dB.
+
+  BB Gain:
+  Overall baseband gain of the device.
+  This setting is available for HackRF in receive mode. Observations lead to a reasonable gain range from 15 to 30dB.
+
+  Antenna:
+  For devices with only one antenna, this may be left blank.
+  Otherwise, the user should specify one of the possible antenna choices.
+
+  Bandwidth:
+  Set the bandpass filter on the radio frontend. To use the default (automatic) bandwidth filter setting, this should be zero.
+
+  See the OsmoSDR project page for more detailed documentation:
+  http://sdr.osmocom.org/trac/wiki/GrOsmoSDR
+  http://sdr.osmocom.org/trac/wiki/rtl-sdr
+  http://sdr.osmocom.org/trac/
+  
+file_format: 1
 """
 
+# MAIN_TMPL = """\
+# <block>
+#   <check>$max_nchan >= \$nchan</check>
+#   <check>\$nchan > 0</check>
+#   <check>$max_mboards >= \$num_mboards</check>
+#   <check>\$num_mboards > 0</check>
+#   <check>\$nchan >= \$num_mboards</check>
+# </block>
+# """
+
 PARAMS_TMPL = """
-  <param>
-    <name>Ch$(n): Frequency (Hz)</name>
-    <key>freq$(n)</key>
-    <value>100e6</value>
-    <type>real</type>
-    <hide>\#if \$nchan() > $n then 'none' else 'all'#</hide>
-  </param>
-  <param>
-  <name>Ch$(n): Freq. Corr. (ppm)</name>
-    <key>corr$(n)</key>
-    <value>0</value>
-    <type>real</type>
-    <hide>\#if \$nchan() > $n then 'none' else 'all'#</hide>
-  </param>
-#if $sourk == 'source':
-  <param>
-    <name>Ch$(n): DC Offset Mode</name>
-    <key>dc_offset_mode$(n)</key>
-    <value>0</value>
-    <type>int</type>
-    <hide>\#if \$nchan() > $n then 'none' else 'all'#</hide>
-    <option>
-      <name>Off</name>
-      <key>0</key>
-    </option>
-    <option>
-      <name>Manual</name>
-      <key>1</key>
-    </option>
-    <option>
-      <name>Automatic</name>
-      <key>2</key>
-    </option>
-  </param>
-  <param>
-    <name>Ch$(n): IQ Balance Mode</name>
-    <key>iq_balance_mode$(n)</key>
-    <value>0</value>
-    <type>int</type>
-    <hide>\#if \$nchan() > $n then 'none' else 'all'#</hide>
-    <option>
-      <name>Off</name>
-      <key>0</key>
-    </option>
-    <option>
-      <name>Manual</name>
-      <key>1</key>
-    </option>
-    <option>
-      <name>Automatic</name>
-      <key>2</key>
-    </option>
-  </param>
-  <param>
-    <name>Ch$(n): Gain Mode</name>
-    <key>gain_mode$(n)</key>
-    <value>False</value>
-    <type>bool</type>
-    <hide>\#if \$nchan() > $n then 'none' else 'all'#</hide>
-    <option>
-      <name>Manual</name>
-      <key>False</key>
-    </option>
-    <option>
-      <name>Automatic</name>
-      <key>True</key>
-    </option>
-  </param>
-#end if
-  <param>
-    <name>Ch$(n): RF Gain (dB)</name>
-    <key>gain$(n)</key>
-    <value>10</value>
-    <type>real</type>
-    <hide>\#if \$nchan() > $n then 'none' else 'all'#</hide>
-  </param>
-  <param>
-    <name>Ch$(n): IF Gain (dB)</name>
-    <key>if_gain$(n)</key>
-    <value>20</value>
-    <type>real</type>
-    <hide>\#if \$nchan() > $n then 'none' else 'all'#</hide>
-  </param>
-  <param>
-    <name>Ch$(n): BB Gain (dB)</name>
-    <key>bb_gain$(n)</key>
-    <value>20</value>
-    <type>real</type>
-    <hide>\#if \$nchan() > $n then 'none' else 'all'#</hide>
-  </param>
-  <param>
-    <name>Ch$(n): Antenna</name>
-    <key>ant$(n)</key>
-    <value></value>
-    <type>string</type>
-    <hide>
-      \#if not \$nchan() > $n
-        all
-      \#elif \$ant$(n)()
-        none
-      \#else
-        part
-      \#end if
-    </hide>
-  </param>
-  <param>
-    <name>Ch$(n): Bandwidth (Hz)</name>
-    <key>bw$(n)</key>
-    <value>0</value>
-    <type>real</type>
-    <hide>
-      \#if not \$nchan() > $n
-        all
-      \#elif \$bw$(n)()
-        none
-      \#else
-        part
-      \#end if
-    </hide>
-  </param>
+- id: freq${n}
+  label: 'Ch${n}: Frequency (Hz)'
+  dtype: real
+  default: 100e6
+  hide: ${'$'}{'none' if (nchan > ${n}) else 'all'}
+- id: corr${n}
+  label: 'Ch${n}: Frequency Correction (ppm)'
+  dtype: real
+  default: 0
+  hide: ${'$'}{'none' if (nchan > ${n}) else 'all'}
+% if sourk == 'source':
+- id: dc_offset_mode${n}
+  label: 'Ch${n}: DC Offset Mode'
+  dtype: int
+  default: 0
+  options: [0, 1, 2]
+  option_labels: [Off, Manual, Automatic]
+  hide: ${'$'}{'none' if (nchan > ${n}) else 'all'}
+- id: iq_balance_mode${n}
+  label: 'Ch${n}: IQ Balance Mode'
+  dtype: int
+  default: 0
+  options: [0, 1, 2]
+  option_labels: [Off, Manual, Automatic]
+  hide: ${'$'}{'none' if (nchan > ${n}) else 'all'}
+- id: gain_mode${n}
+  label: 'Ch${n}: Gain Mode'
+  dtype: bool
+  default: False
+  options: [False, True]
+  option_labels: [Manual, Automatic]
+  hide: ${'$'}{'none' if (nchan > ${n}) else 'all'}
+% endif
+- id: gain${n}
+  label: 'Ch${n}: RF Gain (dB)'
+  dtype: real
+  default: 10
+  hide: ${'$'}{'none' if (nchan > ${n}) else 'all'}
+- id: if_gain${n}
+  label: 'Ch${n}: IF Gain (dB)'
+  dtype: real
+  default: 20
+  hide: ${'$'}{'none' if (nchan > ${n}) else 'all'}
+- id: bb_gain${n}
+  label: 'Ch${n}: BB Gain (dB)'
+  dtype: real
+  default: 20
+  hide: ${'$'}{'none' if (nchan > ${n}) else 'all'}
+- id: ant${n}
+  label: 'Ch${n}: Antenna'
+  dtype: string
+  default: ""
+  hide: ${'$'}{'all' if not (nchan > ${n}) else ('none' if eval('ant' + str(${n})) else 'part')}
+- id: bw${n}
+  label: 'Ch${n}: Bandwidth (Hz)'
+  dtype: real
+  default: 0
+  hide: ${'$'}{'all' if not (nchan > ${n}) else ('none' if eval('bw' + str(${n})) else 'part')}
 """
 
+
 def parse_tmpl(_tmpl, **kwargs):
-  from Cheetah import Template
-  return str(Template.Template(_tmpl, kwargs))
+    from mako.template import Template
+    from mako import exceptions
 
-max_num_mboards = 8
-max_num_channels = max_num_mboards*4
+    try:
+        block_template = Template(_tmpl)
+        return str(block_template.render(**kwargs))
+    except:
+        print(exceptions.text_error_template().render())
 
+MAX_NUM_MBOARDS = 8
+MAX_NUM_CHANNELS = MAX_NUM_MBOARDS * 4
+
 import os.path
 
 if __name__ == '__main__':
-  import sys
-  for file in sys.argv[1:]:
-    head, tail = os.path.split(file)
+    import sys
 
-    if tail.startswith('rtlsdr'):
-      title = 'RTL-SDR'
-      prefix = 'rtlsdr'
-    elif tail.startswith('osmosdr'):
-      title = 'osmocom'
-      prefix = 'osmosdr'
-    else: raise Exception, 'file %s has wrong syntax!'%tail
+    for file in sys.argv[1:]:
+        head, tail = os.path.split(file)
 
-    if tail.endswith ('source.xml'):
-      sourk = 'source'
-      dir = 'out'
-    elif tail.endswith ('sink.xml'):
-      sourk = 'sink'
-      dir = 'in'
-    else: raise Exception, 'is %s a source or sink?'%file
+        if tail.startswith('rtlsdr'):
+            title = 'RTL-SDR'
+            prefix = 'rtlsdr'
+        elif tail.startswith('osmosdr'):
+            title = 'osmocom'
+            prefix = 'osmosdr'
+        else:
+            raise Exception("file {} has wrong syntax!".format(tail))
 
-    params = ''.join([parse_tmpl(PARAMS_TMPL, n=n, sourk=sourk) for n in range(max_num_channels)])
-    open(file, 'w').write(parse_tmpl(MAIN_TMPL,
-      max_nchan=max_num_channels,
-      max_mboards=max_num_mboards,
-      params=params,
-      title=title,
-      prefix=prefix,
-      sourk=sourk,
-      dir=dir,
-    ))
+        if tail.endswith('source.block.yml'):
+            sourk = 'source'
+            direction = 'out'
+        elif tail.endswith('sink.block.yml'):
+            sourk = 'sink'
+            direction = 'in'
+        else:
+            raise Exception("is {} a source or sink?".format(file))
+
+        params = ''.join([
+            parse_tmpl(PARAMS_TMPL, n=n, sourk=sourk)
+            for n in range(MAX_NUM_CHANNELS)
+        ])
+
+        open(file, 'w').write(
+            parse_tmpl(
+                MAIN_TMPL,
+                max_nchan=MAX_NUM_CHANNELS,
+                max_mboards=MAX_NUM_MBOARDS,
+                params=params,
+                title=title,
+                prefix=prefix,
+                sourk=sourk,
+                direction=direction,
+            )
+        )
