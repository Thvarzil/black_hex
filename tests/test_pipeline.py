from generator.pipeline import run_generation, layer_seed


def test_run_generation_without_seed_does_not_raise():
    run_generation()


def test_run_generation_with_southern_hemisphere_seed():
    # seed=0 produces int(val*10)%2==0 → hemisphereIsSouth=True
    run_generation(seed=0)


def test_run_generation_with_northern_hemisphere_seed():
    # seed=1 produces int(val*10)%2==1 → hemisphereIsSouth stays False
    run_generation(seed=1)


def test_layer_seed_is_deterministic_and_unique_per_layer():
    assert layer_seed(42, "elevation") == layer_seed(42, "elevation")
    assert layer_seed(42, "elevation") != layer_seed(42, "moisture")
