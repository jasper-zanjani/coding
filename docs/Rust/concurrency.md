# Concurrency

--8<-- "includes/rs/concurrency/info.md"

## Channels

--8<-- "includes/rs/concurrency/channels.md"

## Mutex

--8<-- "includes/rs/concurrency/mutex.md"

## Atomic reference counting

--8<-- "includes/rs/concurrency/atomics.md"

## Cell

[`Cell`][Cell] and [`RefCell`][RefCell] are used to implement _interior mutability_ (1).
{: .annotate }

1.  

    --8<-- "includes/rs/concurrency/atomics-locks/interior-mutability"
