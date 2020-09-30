# IBM Cloud Object Storage (IBM COS)

![Captura de Tela 2020-07-10 às 16 09 39](https://user-images.githubusercontent.com/17646546/87189897-dcfbee80-c2c7-11ea-9879-e3b62fdbcd51.png)

IBM Cloud Object Storage is a cloud storage service. Client applications use the S3 API interface to write objects to IBM COS.
This project worked with IBM COS using python programming language. So, used [IBM COS SDK for Python Documentation](https://ibm.github.io/ibm-cos-sdk-python/index.html).

## Credentials

You’ll notice that the credentials aren't working because are fake ones.  

~~~python
cos = {
  "apikey": "fake-apikey-b6ZTDS18TDMOoLgTyU",
  "iam_serviceid_crn": "fake-serviceid-crn:v1:bluemix:public:iam-identity",
  "endpoints": "https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints",
  "ibm_auth_endpoint": "https://iam.cloud.ibm.com/"
}
~~~

## Quick Usage

### Docker Build

Build an image called **data-ibm**:

```bash
$ docker build -t data-ibm .
```

### Docker Run

Run the image **data-ibm**:

```bash
$ docker run data-ibm
```

## Features

In this project, we have three main features.

1. Upload CSV files to bucket;
2. Merge these files;
3. Put files on bucket.

---

## Clone

Now that you're more familiar with this data-ibm-cos repository, go ahead and clone it.

