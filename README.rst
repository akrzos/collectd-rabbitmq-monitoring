Collectd Rabbitmq Monitoring
============================

Overview
--------

This plugin provides metrics from yoru running Rabbitmq cluster via
the rabbitmq management plugin API.

Sample Graph
------------

.. figure:: https://github.com/akrzos/collectd-rabbitmq-monitoring/blob/master/sample-collectd-rabbitmq-monitoring.png
   :alt: Sample Graph

Configuration
-------------

1. Assuming you have collectd installed already, append the following
   plugin details to your collectd.conf config file.  Adjust the
   configuration items (interval, host, port, username, password,
   message_count) as you see fit.

   ::

       ```
       <LoadPlugin python>
         Globals true
       </LoadPlugin>

       <Plugin python>
         LogTraces true
         Interactive false
         Import "collectd_rabbitmq_monitoring"
         <Module collectd_rabbitmq_monitoring>
           # Adjust these parameters for your install:
           interval 10
           host "overcloud-controller-0.internalapi.localdomain"
           port 15672
           username guest
           password guest
           # Omit message_count if you do not want to count any messages on
           # specific queues.
           message_count "metering.sample" "notifications.info"
         </Module>
       </Plugin>
       ```

2. Install the Rabbitmq management plugin

   ::

       ```
       [root@overcloud-controller-0 ~]# rabbitmq-plugins enable rabbitmq_management
       ```

3. Install plugin

   ::

       ```
       [root@overcloud-controller-0 ~]# pip install collectd-rabbitmq-monitoring
       ```

4. Restart collectd

   ::

       [root@overcloud-controller-0 ~]# systemctl restart collectd

5. View metrics on Rabbitmq in your TSDB

Resources
---------

1. `Rabbitmq.com`_
2. `Collectd.org`_

.. _Rabbitmq.com: https://www.rabbitmq.com/
.. _Collectd.org: https://collectd.org/
