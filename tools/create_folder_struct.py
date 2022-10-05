from utils import checkMigrationFolderStruct, createMigrationFolderStruct

if not checkMigrationFolderStruct():
    createMigrationFolderStruct()