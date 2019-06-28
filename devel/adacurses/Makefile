# Created by: olgeni@FreeBSD.org
# $FreeBSD: head/devel/adacurses/Makefile 498881 2019-04-14 09:31:17Z amdmi3 $

PORTNAME=	adacurses
DISTVERSION=	20180127
PORTREVISION=	1
CATEGORIES=	devel
MASTER_SITES=	ftp://ftp.invisible-island.net/AdaCurses/
DISTNAME=	AdaCurses-${DISTVERSION}

MAINTAINER=	ports@FreeBSD.org
COMMENT=	Ada95 bindings for ncurses

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/README

USES=		ada gmake pkgconfig tar:tgz

GNU_CONFIGURE=	yes
CONFIGURE_ARGS=	--with-ada-include=${PREFIX}/include/adacurses \
		--with-ada-objects=${PREFIX}/lib/adacurses \
		--libdir=${PREFIX}/lib/adacurses \
		--enable-widec
PORTDOCS=	ada Ada95.html
PLIST_SUB=	atic=adacurses/terminal_interface-curses

OPTIONS_DEFINE=	DOCS

post-patch:
	@${REINPLACE_CMD} -e '/(INSTALL_PROG)/d' -e 's|@ADAGEN_LDFLAGS@||' \
		${WRKSRC}/gen/Makefile.in
	@${REINPLACE_CMD} -e '/pragma Linker_Options/d' \
		${WRKSRC}/gen/terminal_interface-curses.ads.m4 \
		${WRKSRC}/gen/terminal_interface-curses-menus.ads.m4 \
		${WRKSRC}/gen/terminal_interface-curses-forms.ads.m4 \
		${WRKSRC}/gen/terminal_interface-curses-panels.ads.m4
	@${REINPLACE_CMD} -e 's|@LIBS@|@LIBS@ -lmenu -lform -lpanel|' \
		${WRKSRC}/samples/Makefile.in

post-install:
	${INSTALL_SCRIPT} ${WRKSRC}/gen/adacurses-config \
		${STAGEDIR}${PREFIX}/bin/
	@${MKDIR} ${STAGEDIR}${PREFIX}/lib/gnat
	${INSTALL_DATA} ${FILESDIR}/adacurses.gpr \
		${STAGEDIR}${PREFIX}/lib/gnat/

do-install-DOCS-on:
	(cd ${WRKSRC}/doc && ${SETENV} ${MAKE_ENV} \
		${MAKE_CMD} ${MAKE_ARGS} THIS=${PORTNAME} install.html)

.include <bsd.port.mk>
