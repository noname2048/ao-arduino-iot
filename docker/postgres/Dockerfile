# https://postgresql.kr/blog/when_useing_docker_official_postgres_image.html
# 다음을 참조하여 작성하였습니다.
FROM postgres:12
RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime && \
    sed -i 's/# ko_KR.UTF-8 UTF-8/ko_KR.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG=ko_KR.utf8 \
    LC_COLLATE=C \
    POSTGRES_INITDB_ARGS=--data-checksums
