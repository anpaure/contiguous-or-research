# Independent audit: pair-union binary-host compiler

Date: 2026-09-08. Reviewer: Codex subagent `exact_b_induction`.

Reviewed source:
`scratch/EXACT_PAIR_UNION_BINARY_HOST_COMPILER_20260908.md`.

Verdict: Sections 2–5 are valid as an exact finite theorem for the supplied
domains. This is an internal mathematical review, not external or formal
verification. No mathematical execution was needed. Historical source
censuses in Section 6 were not independently recomputed in this review.

## Individual legality is necessary even under simultaneous shrinkage

This point can be stated more strongly than the source's immediate
necessity argument. Suppose `A_j subseteq E_j` at every position and
`A_i union A_{i+1}=E_i union E_{i+1}`. Then

\[
 E_i\cup E_{i+1}
 =A_i\cup A_{i+1}
 \subseteq A_i\cup E_{i+1}
 \subseteq E_i\cup E_{i+1}.
\]

Hence both inclusions are equalities. Thus the installed label `A_i` is
individually legal against the *original* neighbour even when that
neighbour was also shrunk. The analogous equality holds on the other side.
There are no jointly successful shrinkages that are incorrectly rejected
by the individual-host test. The monotone condition `A_j subseteq E_j` is
essential here and is explicitly part of the setup.

## Pair conflicts suffice

Every protected equation involves exactly one adjacent pair. With no
selected endpoint the equation is unchanged; with one it follows from
individual legality; with two it follows from the compatibility test.
Same-position conflicts enforce injectivity. No equation involves three
replacement choices, so the option-conflict description has no missing
higher-order constraint.

One binary variable per two-element domain makes its two choices mutually
exclusive and exhaustive. Incompatibilities forbid literal pairs and hence
are 2-CNF clauses. Fixed single-element domains are handled by unit clauses
or immediate conflict. Restricting a larger host domain to two options is
explicitly acknowledged as a restriction; exactness is not incorrectly
claimed for all original hosts.

## Longer intervals and one-letter-only targets

An interval of length at least two is the union of its adjacent pair
unions. Therefore `DA=DE` preserves that interval's exact union at its
original position. It does **not** preserve a target whose only original
witnesses are single letters at replaced positions.

The source handles this correctly: Section 4 requires every target outside
the replacement family to have a multi-letter witness, and explicitly
requires adding an otherwise lost one-letter-only target to the replacement
family or supplying a separate preserved witness. Its rank-six-envelope
k17 application includes every rank-at-most-six target in that family, so
it does not silently assume original envelope letters survive.

The all-target result is therefore valid with its full hypotheses. It
supplies no missing source construction, no automatic binary host domains,
and no free opening of the cyclic case.
