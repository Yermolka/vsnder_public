DROP INDEX "per_user_picture_unique";

ALTER TABLE "message"
DROP COLUMN "picture";

ALTER TABLE "message"
DROP COLUMN "media_type";

ALTER TABLE "message"
ADD COLUMN "file_id" INT REFERENCES "file" ON DELETE CASCADE;

ALTER TABLE "user"
DROP COLUMN "has_avatar";

ALTER TABLE "user"
ADD COLUMN "file_id" INT REFERENCES "file" ON DELETE SET NULL;
