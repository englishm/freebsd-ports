#!/bin/sh
# $FreeBSD$

if [ -f ${WRKDIRPREFIX}${REALCURDIR}/Makefile.inc ]; then
	exit
fi

tempfile=`/usr/bin/mktemp -t checklist`

if [ "${BATCH}" ]; then
	if [ "${PHP4_OPTIONS}" ]; then
		set ${PHP4_OPTIONS}
	else
		set \"zlib\" \"MySQL\"
	fi
else
	/usr/bin/dialog --title "configuration options" --clear \
		--checklist "\n\
Please select desired options:" -1 -1 16 \
GD		"GD library support" OFF \
zlib		"zlib library support" ON \
mcrypt		"Encryption support" OFF \
mhash		"Crypto-hashing support" OFF \
pdflib		"pdflib support" OFF \
IMAP		"IMAP support" OFF \
MySQL		"MySQL database support" ON \
PostgreSQL	"PostgreSQL database support" OFF \
SybaseDB	"Sybase/MS-SQL database support (DB-lib)" OFF \
SybaseCT	"Sybase/MS-SQL database support (CT-lib)" OFF \
Interbase	"Interbase 6 database support (Firebird)" OFF \
dBase		"dBase database support" OFF \
OpenLDAP1	"OpenLDAP 1.x support" OFF \
OpenLDAP2	"OpenLDAP 2.x support" OFF \
OpenSSL		"OpenSSL support" OFF \
SNMP		"SNMP support" OFF \
XML		"XML support" OFF \
XSLT		"Sablotron support (implies XML and iconv)" OFF \
DOMXML		"DOM support" OFF \
FTP		"File Transfer Protocol support" OFF \
CURL		"CURL support" OFF \
gettext		"gettext library support" OFF \
iconv		"iconv support" OFF \
pspell		"pspell support" OFF \
mbregex		"multibyte regular expressions module" OFF \
mbstring	"multibyte string module" OFF \
YP		"YP/NIS support" OFF \
BCMath		"BCMath support" OFF \
Hyperwave	"Hyperwave support" OFF \
ming		"ming library support" OFF \
sockets		"sockets support" OFF \
sysvsem		"System V semaphore support" OFF \
sysvshm		"System V shared memory support" OFF \
transsid	"Transparent session id" OFF \
2> $tempfile

	retval=$?

	if [ -s $tempfile ]; then
		set `cat $tempfile`
	fi
	rm -f $tempfile

	case $retval in
		0)	if [ -z "$*" ]; then
				echo "Nothing selected"
			fi
			;;
		1)	echo "Cancel pressed."
			exit 1
			;;
	esac
fi

${MKDIR} ${WRKDIRPREFIX}${REALCURDIR}
exec > ${WRKDIRPREFIX}${REALCURDIR}/Makefile.inc

while [ "$1" ]; do
	case $1 in
		\"GD\")
			echo "LIB_DEPENDS+=	gd.2:\${PORTSDIR}/graphics/gd"
			echo "LIB_DEPENDS+=	freetype.7:\${PORTSDIR}/print/freetype2"
			echo "LIB_DEPENDS+=	png.5:\${PORTSDIR}/graphics/png"
			echo "LIB_DEPENDS+=	jpeg.9:\${PORTSDIR}/graphics/jpeg"
			echo "CONFIGURE_ARGS+=--with-gd=\${PREFIX} \\"
			echo "		--with-freetype-dir=\${PREFIX} \\"
			echo "		--with-jpeg-dir=\${PREFIX} \\"
			echo "		--with-png-dir=\${PREFIX}"
			;;
		\"zlib\")
			echo "CONFIGURE_ARGS+=--with-zlib"
			ZLIB=1
			;;
		\"mcrypt\")
			echo "LIB_DEPENDS+=	mcrypt.6:\${PORTSDIR}/security/libmcrypt"
			echo "CONFIGURE_ARGS+=--with-mcrypt=\${PREFIX}"
			;;
		\"mhash\")
			echo "LIB_DEPENDS+=	mhash.2:\${PORTSDIR}/security/mhash"
			echo "CONFIGURE_ARGS+=--with-mhash=\${PREFIX}"
			;;
		\"pdflib\")
			echo "LIB_DEPENDS+=	pdf.3:\${PORTSDIR}/print/pdflib3"
			echo "LIB_DEPENDS+=	jpeg.9:\${PORTSDIR}/graphics/jpeg"
			echo "LIB_DEPENDS+=	png.5:\${PORTSDIR}/graphics/png"
			echo "LIB_DEPENDS+=	tiff.4:\${PORTSDIR}/graphics/tiff"
			echo "CONFIGURE_ARGS+=--with-pdflib=\${PREFIX} \\"
			echo "		--with-zlib-dir=/usr \\"
			echo "		--with-jpeg-dir=\${PREFIX} \\"
			echo "		--with-png-dir=\${PREFIX} \\"
			echo "		--with-tiff-dir=\${PREFIX}"
			;;
		\"IMAP\")
			echo "LIB_DEPENDS+=	c-client4.8:\${PORTSDIR}/mail/cclient"
			echo "CONFIGURE_ARGS+=--with-imap=\${PREFIX}"
			;;
		\"MySQL\")
			echo "LIB_DEPENDS+=	mysqlclient.10:\${PORTSDIR}/databases/mysql323-client"
			echo "CONFIGURE_ARGS+=--with-mysql=\${PREFIX}"
			;;
		\"PostgreSQL\")
			echo "LIB_DEPENDS+=	pq.2:\${PORTSDIR}/databases/postgresql7"
			if [ -x ${PREFIX}/pgsql/bin/postgres -a ! -x ${PREFIX}/bin/postgres ]; then
				PGPREFIX=${PREFIX}/pgsql
			else
				PGPREFIX=${PREFIX}
				echo "CFLAGS+=-I\${PREFIX}/include/pgsql"
			fi
			echo "PGPREFIX=${PGPREFIX}"
			echo "CONFIGURE_ARGS+=--with-pgsql=\${PGPREFIX}"
			if /usr/bin/ldd ${PGPREFIX}/bin/postgres 2> /dev/null | /usr/bin/grep -q "libssl"; then
				echo "USE_OPENSSL=	yes"
				LIBS="${LIBS} -L\${OPENSSLBASE}/lib -lcrypto -lssl"
			fi
			;;
		\"SybaseDB\")
			echo "LIB_DEPENDS+=	sybdb.0:\${PORTSDIR}/databases/freetds"
			echo "CONFIGURE_ARGS+=--with-sybase=\${PREFIX}"
			if [ "$SYBASECT" ]; then
				echo "SybaseDB and SybaseCT are mutually exclusive." > /dev/stderr
				rm -f ${WRKDIRPREFIX}${REALCURDIR}/Makefile.inc
				exit 1
			fi
			SYBASEDB=1
			;;
		\"SybaseCT\")
			echo "LIB_DEPENDS+=	ct.0:\${PORTSDIR}/databases/freetds"
			echo "CONFIGURE_ARGS+=--with-sybase-ct=\${PREFIX}"
			if [ "$SYBASEDB" ]; then
				echo "SybaseDB and SybaseCT are mutually exclusive." > /dev/stderr
				rm -f ${WRKDIRPREFIX}${REALCURDIR}/Makefile.inc
				exit 1
			fi
			SYBASECT=1
			;;
		\"Interbase\")
			echo "LIB_DEPENDS+=	gds.1:\${PORTSDIR}/databases/firebird"
			echo "CONFIGURE_ARGS+=--with-interbase=\${PREFIX}/firebird"
			;;
		\"dBase\")
			echo "CONFIGURE_ARGS+=--with-dbase"
			;;
		\"OpenLDAP1\")
			echo "LIB_DEPENDS+=	ldap.1:\${PORTSDIR}/net/openldap"
			echo "LIB_DEPENDS+=	lber.1:\${PORTSDIR}/net/openldap"
			echo "CONFIGURE_ARGS+=--with-ldap=\${PREFIX}"
			if [ "$OPENLDAP2" ]; then
				echo "OpenLDAP1 and OpenLDAP2 are mutually exclusive." > /dev/stderr
				rm -f ${WRKDIRPREFIX}${REALCURDIR}/Makefile.inc
				exit 1
			fi
			if [ -f /usr/lib/libkrb.a -a -f /usr/lib/libdes.a -a ! -L /usr/lib/libdes.a ]; then
				LIBS="${LIBS} -lkrb -ldes -L\${PREFIX}/lib"
			fi
			OPENLDAP1=1
			;;
		\"OpenLDAP2\")
			echo "LIB_DEPENDS+=	ldap.2:\${PORTSDIR}/net/openldap2"
			echo "LIB_DEPENDS+=	lber.2:\${PORTSDIR}/net/openldap2"
			echo "CONFIGURE_ARGS+=--with-ldap=\${PREFIX}"
			if [ "$OPENLDAP1" ]; then
				echo "OpenLDAP1 and OpenLDAP2 are mutually exclusive." > /dev/stderr
				rm -f ${WRKDIRPREFIX}${REALCURDIR}/Makefile.inc
				exit 1
			fi
			if [ -f /usr/lib/libkrb.a -a -f /usr/lib/libdes.a -a ! -L /usr/lib/libdes.a ]; then
				LIBS="${LIBS} -lkrb -ldes -L\${PREFIX}/lib"
			fi
			OPENLDAP2=1
			;;
		\"OpenSSL\")
			echo "USE_OPENSSL=yes"
			echo "CONFIGURE_ARGS+=--with-openssl=\${OPENSSLBASE}"
			;;
		\"SNMP\")
			echo "LIB_DEPENDS+=	snmp.4:\${PORTSDIR}/net/net-snmp"
			echo "CONFIGURE_ARGS+=--with-snmp=\${PREFIX} --enable-ucd-snmp-hack"
			echo "USE_OPENSSL=	yes"
			LIBS="${LIBS} -L\${OPENSSLBASE}/lib -lcrypto -lssl"
			;;
		\"XML\")
			echo "LIB_DEPENDS+=	expat.2:\${PORTSDIR}/textproc/expat2"
			echo "CONFIGURE_ARGS+=--with-xml --with-expat-dir=\${PREFIX}"
			XML=1
			;;
		\"XSLT\")
			echo "LIB_DEPENDS+=	sablot.70:\${PORTSDIR}/textproc/sablotron"
			echo "CONFIGURE_ARGS+=--with-sablot=\${PREFIX}"
			echo "CONFIGURE_ARGS+=--with-expat-dir=\${PREFIX}"
			if [ -z "$XML" ]; then
				set $* \"XML\"
			fi
			if [ -z "$ICONV" ]; then
				set $* \"iconv\"
			fi
			;;
		\"DOMXML\")
			echo "LIB_DEPENDS+=	xml2.5:\${PORTSDIR}/textproc/libxml2"
			echo "CONFIGURE_ARGS+=--with-dom=\${PREFIX}"
			;;
		\"FTP\")
			echo "CONFIGURE_ARGS+=--enable-ftp"
			;;
		\"CURL\")
			echo "CONFIGURE_ARGS+=--with-curl=\${PREFIX}"
			echo "BUILD_DEPENDS+=	\${PREFIX}/lib/libcurl.a:\${PORTSDIR}/ftp/curl"
                        ;;
		\"gettext\")
			echo "LIB_DEPENDS+=	intl.1:\${PORTSDIR}/devel/gettext"
			echo "CONFIGURE_ARGS+=--with-gettext=\${PREFIX}"
			;;
		\"iconv\")
			echo "LIB_DEPENDS+=	iconv.2:\${PORTSDIR}/converters/iconv"
			echo "CONFIGURE_ARGS+=--with-iconv=\${PREFIX}"
			ICONV=1
			;;
		\"pspell\")
			echo "LIB_DEPENDS+=	pspell.4:\${PORTSDIR}/textproc/pspell"
			echo "CONFIGURE_ARGS+=--with-pspell=\${PREFIX}"
			;;
		\"mbregex\")
			${CAT} << EOF
MASTER_SITES+=	ftp://night.fminn.nagano.nagano.jp/php4/
DISTFILES=	\${DISTNAME}\${EXTRACT_SUFX} php4_mbregex-1.2.1.tar.gz
CONFIGURE_ARGS+=--enable-mbregex
BUILD_DEPENDS+=	automake:\${PORTSDIR}/devel/automake
BUILD_DEPENDS+=	autoconf:\${PORTSDIR}/devel/autoconf
POSTEXTRACT+=	post-extract-mbregex

post-extract-mbregex:
	[ -d \${WRKDIR}/mbregex ] && \\
	(cd \${WRKSRC}; \\
	 \${MV} ${WRKDIR}/mbregex ext)

EOF
			;;
		\"mbstring\")
			echo "CONFIGURE_ARGS+=--enable-mbstring"
			;;
		\"YP\")
			echo "CONFIGURE_ARGS+=--enable-yp"
			;;
		\"BCMath\")
			echo "CONFIGURE_ARGS+=--enable-bcmath"
			;;
		\"Hyperwave\")
			echo "CONFIGURE_ARGS+=--with-hyperwave=yes"
			;;
		\"ming\")
			echo "LIB_DEPENDS+=	ming.3:\${PORTSDIR}/graphics/ming"
			echo "CONFIGURE_ARGS+=--with-ming=\${PREFIX}"
			;;
		\"sockets\")
			echo "CONFIGURE_ARGS+=--enable-sockets"
			;;
		\"sysvsem\")
			echo "CONFIGURE_ARGS+=--enable-sysvsem"
			;;
		\"sysvshm\")
			echo "CONFIGURE_ARGS+=--enable-sysvshm"
			;;
		\"transsid\")
			echo "CONFIGURE_ARGS+=--enable-trans-sid"
			;;
		*)
			echo "Invalid option(s): $*" > /dev/stderr
			rm -f ${WRKDIRPREFIX}${REALCURDIR}/Makefile.inc
			exit 1
			;;
	esac
	shift
done

if [ "${LIBS}" ]; then
	echo "CONFIGURE_ENV+=	LIBS='${LIBS}'"
fi
