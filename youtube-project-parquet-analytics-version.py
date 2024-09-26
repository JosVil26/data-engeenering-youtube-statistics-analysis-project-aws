import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql import functions as SqlFuncs

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1727202739676 = glueContext.create_dynamic_frame.from_catalog(database="youtube-project-cleaned", table_name="cleaned_statistics_reference_data", transformation_ctx="AWSGlueDataCatalog_node1727202739676")

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1727202770957 = glueContext.create_dynamic_frame.from_catalog(database="youtube-project-cleaned", table_name="raw_statistics", transformation_ctx="AWSGlueDataCatalog_node1727202770957")

# Script generated for node Join
Join_node1727202843687 = Join.apply(frame1=AWSGlueDataCatalog_node1727202770957, frame2=AWSGlueDataCatalog_node1727202739676, keys1=["category_id"], keys2=["id"], transformation_ctx="Join_node1727202843687")

# Script generated for node Drop Duplicates
DropDuplicates_node1727216702027 =  DynamicFrame.fromDF(Join_node1727202843687.toDF().dropDuplicates(["video_id", "trending_date", "title", "channel_title", "category_id", "publish_time", "tags", "views", "likes", "dislikes", "comment_count", "thumbnail_link", "comments_disabled", "ratings_disabled", "video_error_or_removed", "description", "region", "kind", "id", "snippet_channelid", "snippet_title", "snippet_assignable"]), glueContext, "DropDuplicates_node1727216702027")

# Script generated for node Amazon S3
AmazonS3_node1727203608058 = glueContext.getSink(path="s3://youtube-project-analytics-dev", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=["region", "category_id"], enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1727203608058")
AmazonS3_node1727203608058.setCatalogInfo(catalogDatabase="youtube-project-analytics",catalogTableName="final_analytics")
AmazonS3_node1727203608058.setFormat("glueparquet", compression="snappy")
AmazonS3_node1727203608058.writeFrame(DropDuplicates_node1727216702027)
job.commit()