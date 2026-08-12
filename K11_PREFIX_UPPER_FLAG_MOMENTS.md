# Exact upper-flag moments for the forced `k=11` prefix

## 1. The rank-seven degree identity

Fix a rank-seven mask `U` and let

```text
S_U = {T subset U : |T|=6}.
```

There are seven vertices in `S_U`.  A Johnson edge has both endpoints in
`S_U` exactly when its upper union colour is `U`.  Let

```text
m_U = number of selected real edges internal to S_U,
b_U = number of selected real edges crossing S_U to its complement,
e_U = number of selected dummy endpoint edges incident with S_U.
```

Summing the selected degree-two equations of the seven vertices gives the
exact identity

\[
 2m_U+b_U+e_U=14.                         \tag{1}
\]

This needs neither connectivity nor a bound on `m_U`.  In the full solution
the upper-colour coverage clause independently gives `m_U>=1`.

## 2. Exact support size

The seven vertices induce `K_7`, hence have 21 internal Johnson edges.  Each
rank-six vertex has 30 Johnson neighbours, six internal and 24 external.
Therefore there are

```text
21 internal edges, counted twice =  42 literal occurrences
168 real cut edges, counted once  = 168 literal occurrences
7 dummy endpoint edges           =   7 literal occurrences
                                      ---
                                      217 total occurrences.
```

An exact-14 counter over this multiset is precisely (1).  Repeating an
internal edge literal is sound: the audited cardinality encoding is correct
for an arbitrary input vector, and identifying two input variables by
substituting the same literal simply restricts it to the assignments where
those inputs agree.  The resulting arithmetic contribution is `2x`.

## 3. Forced-prefix specialization

Every adjacent pair in the fixed canonical prefix supplies an explicit
rank-seven upper colour

```text
E|F, F|G, G|H, H|I.
```

Some may coincide, so the implementation deduplicates them.  For each unique
colour it adds (1).  These redundant equalities globally couple the chosen
prefix transitions to every edge incident with the same seven-set and to both
unknown endpoint flags.

Enable them with

```text
RECOMBINE_PREFIX_UPPER_MOMENTS=1.
```

The option requires WLOG canonicalization, ordered orientation, `k=11`, and
`rank=6`.  It can be combined independently with the lower prefix moments and
the omitted-colour moment.

## 4. Scope

Equation (1) is valid even for a disconnected degree-two relaxation.  The
scope guard exists because the current implementation obtains the list of
upper colours from the directed canonical prefix, not because the theorem
requires a Hamilton path.
