from rest_framework import serializers

from receipts.models import Receipts


class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipts
        fields = ['id', 'user', 'title', 'content', 'ingredients', 'image_main']

    def validate_description(self, value):
        if len(value) > 250:
            raise serializers.ValidationError(
                'Слишком большое описание допустимо лишь 250 символов. Для отправки данных пожайлуста исправьте')

    # def validate(self, data):
    #     description = data.get('description',None)
    #     print(data.get('description',None))
    #     if description == "":
    #         description = None
    #     if description is None:
    #         raise serializers.ValidationError('Поле описание должно быть заполнено')
    #     return data
