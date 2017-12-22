# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aggregator', '0013_auto_20171218_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layer',
            name='type',
            field=models.CharField(default=b'OGC:WMS', max_length=32, choices=[(b'OGC:CSW', b'Catalogue Service for the Web (CSW)'), (b'OGC:WMS', b'Web Map Service (WMS)'), (b'OGC:WMTS', b'Web Map Tile Service (WMTS)'), (b'OSGeo:TMS', b'Tile Map Service (TMS)'), (b'ESRI:ArcGIS:MapServer', b'ArcGIS REST MapServer'), (b'ESRI:ArcGIS:ImageServer', b'ArcGIS REST ImageServer'), (b'Hypermap:WorldMap', b'Harvard WorldMap'), (b'Hypermap:WorldMap2', b'ZJU Acadamic Map Publishing Platform'), (b'Hypermap:WARPER', b'Mapwarper')]),
        ),
        migrations.AlterField(
            model_name='service',
            name='type',
            field=models.CharField(default=b'OGC:WMS', max_length=32, choices=[(b'OGC:CSW', b'Catalogue Service for the Web (CSW)'), (b'OGC:WMS', b'Web Map Service (WMS)'), (b'OGC:WMTS', b'Web Map Tile Service (WMTS)'), (b'OSGeo:TMS', b'Tile Map Service (TMS)'), (b'ESRI:ArcGIS:MapServer', b'ArcGIS REST MapServer'), (b'ESRI:ArcGIS:ImageServer', b'ArcGIS REST ImageServer'), (b'Hypermap:WorldMap', b'Harvard WorldMap'), (b'Hypermap:WorldMap2', b'ZJU Acadamic Map Publishing Platform'), (b'Hypermap:WARPER', b'Mapwarper')]),
        ),
    ]
