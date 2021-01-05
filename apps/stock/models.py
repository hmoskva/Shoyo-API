from django.db import models


class Stock(models.Model):
    """Model definition for Stock."""
    LARGE = 'L'
    MEDIUM = 'M'
    SMALL = 'S'

    SIZE_CHOICES = [
        (LARGE, "Large"),
        (MEDIUM, "Medium"),
        (SMALL, "Small"),
    ]

    flavour = models.ForeignKey(
        'flavours.Flavour', on_delete=models.SET_NULL, null=True, related_name="stock")
    size = models.CharField(max_length=1, choices=SIZE_CHOICES,  default=LARGE)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        """Meta definition for Stock."""

        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'
        constraints = [
            models.UniqueConstraint(
                fields=["flavour", "size"], name="unique_flavour_size"
            ),
        ]

    def __str__(self):
        """Unicode representation of Stock."""
        return str(self.id)
