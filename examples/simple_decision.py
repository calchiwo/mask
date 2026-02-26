from datetime import datetime

from mask import (
    Identity,
    Context,
    Policy,
    DecisionEngine,
)
from mask.identity import ExposureLevel, Stability
from mask.context import RiskProfile


identity = Identity(
    mask_id="dev-001",
    exposure=ExposureLevel.LOW,
    stability=Stability.ROTATING,
    region_intent="eu",
)

context = Context(
    app="api_testing",
    domain="example.com",
    timestamp=datetime.utcnow(),
    network="coffee-shop-wifi",
    risk=RiskProfile.MEDIUM,
)

policy = Policy.default()
engine = DecisionEngine(policy)

decision = engine.decide(identity, context)

print(decision)