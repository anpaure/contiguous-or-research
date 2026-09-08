# `K5` root-link census: upper coverage is automatic, fixed boundaries are not

**Date:** 2026-08-02  
**Status:** exact `K5` theorem plus complete `O3` C++ census.  This is a
small-parameter audit of the root-link proposal.  It does not prove the
corresponding statement in general odd dimension.

## 0. Outcome

Put `k=5`, `r=3`.  There are exactly `60` perfect containment matchings

\[
 \mu:{[5]\choose2}\longrightarrow {[5]\choose3},\qquad L\subset\mu(L).
\]

The complete census gives two sharply different conclusions.

1. **Positive upper result.** Every one of the `60` root-link digraphs has a
   directed Hamilton path, and every directed Hamilton path in every one of
   them covers all five rank-four upper colours.  Thus at `K5`, once a rooted
   Hamilton path exists, upper surjectivity costs nothing.
2. **Negative fixed-boundary result.** An arbitrary matching cannot be frozen
   before the endpoint request.  Of the `1200` relevant fixed-boundary
   requests, only `600` admit any directed Hamilton path.  The other `600`
   fail before upper coverage is considered.

Consequently the weak conjecture

> every perfect containment matching has some upper-surjective rooted
> Hamilton path

is true at `K5`, while the stronger endpoint-universal conjecture is false.
The matching and the protected boundary must be selected jointly.

## 1. Exact owner-coordinate form

For each owner `T in ([5] choose 3)`, write its matched root as

\[
                 \mu^{-1}(T)=T\setminus\{\rho(T)\},
                 \qquad \rho(T)\in T.                    \tag{1.1}
\]

The ten sets `T minus {rho(T)}` must be pairwise distinct.  The root-link
arcs are exactly

\[
       \boxed{T\longrightarrow T-\rho(T)+x\qquad(x\notin T).} \tag{1.2}
\]

There are two choices of `x`, so every root-link digraph is directed
two-in/two-out.  The immediate upper colour on this arc is

\[
       T\cup(T-\rho(T)+x)=T\cup\{x\}.                    \tag{1.3}
\]

This is the representation used by the audit; no alternating middle-levels
incidence variables are needed.

## 2. At `K5`, every rooted Hamilton path is upper-surjective

### Theorem 2.1

For every perfect containment matching `mu`, every directed Hamilton path
in its root-link graph covers all five rank-four upper colours.

### Proof

Let

\[
                        T_0,T_1,\ldots,T_9               \tag{2.1}
\]

be a directed Hamilton path and let

\[
                        M=\mu^{-1}(T_9)                   \tag{2.2}
\]

be its unused terminal root.  The nine edge intersections are precisely
the other nine roots.

Fix a coordinate `z`.  Exactly six rank-three owners contain `z`, while
four omit it.  In the binary incidence word

\[
                         1_{z\in T_0}\cdots1_{z\in T_9}, \tag{2.3}
\]

the number of adjacent `11` pairs equals the number of used rank-two roots
containing `z`, namely

\[
                         4-1_{z\in M}.                    \tag{2.4}
\]

Hence the number `a` of positive runs is

\[
                         a=6-(4-1_{z\in M})
                           =2+1_{z\in M}.                 \tag{2.5}
\]

If the upper colour `[5] minus {z}` were absent, no two consecutive owners
could both omit `z`.  All four zeros in (2.3) would be singleton zero runs,
so their run count would be `b=4`.

Run counts in a binary word differ by at most one.  If `z notin M`, then
`a=2,b=4`, impossible.  If `z in M`, then `a=3,b=4`; this forces the word to
start and end in zero.  But `z in M subset T_9`, so it ends in one, again a
contradiction.  Thus `[5] minus {z}` occurs.  This holds for every `z`.
\(\square\)

This explains the exact audit equality

\[
             \#\{\text{Hamilton paths}\}
             =\#\{\text{upper-surjective Hamilton paths}\}=2280. \tag{2.6}
\]

## 3. Petersen classification of all matchings

Identify an owner `T` with its two-set complement.  The matching becomes a
permutation

\[
     \sigma(L)=[5]\setminus\mu(L)                         \tag{3.1}
\]

of the ten two-sets, and `L` is disjoint from `sigma(L)`.  Thus every arrow
of `sigma` is an edge of the Petersen graph.  The `60` matchings split into
exactly three cycle types:

| Petersen permutation type | matchings | Hamilton paths per matching | reachable ordered endpoint pairs | reachable relevant fixed boundaries |
|---|---:|---:|---:|---:|
| `2+2+2+2+2` | 6 | 60 | 30 | 0 of 20 |
| `2+8` | 30 | 32 | 20 | 4 of 20 |
| `5+5` | 24 | 40 | 40 | 20 of 20 |

In particular, a `5+5` matching supports every relevant protected boundary,
whereas a five-transposition matching supports none.  The finite lesson is
not that endpoints are intrinsically impossible; it is that `mu` cannot be
chosen independently of them.

## 4. A literal fixed-boundary counterexample

Here is one `2+8` matching.  Each owner is followed by its matched root:

\[
\begin{array}{c|cccccccccc}
T&012&013&023&123&014&024&124&034&134&234\\ \hline
\mu^{-1}(T)&12&13&03&23&01&02&14&04&34&24.
\end{array}                                                \tag{4.1}
\]

Request the initial owner

\[
                         C=024,                            \tag{4.2}
\]

terminal root and owner

\[
                         M=01,\qquad B=014,                \tag{4.3}
\]

and duplicated root

\[
                         D=04.                             \tag{4.4}
\]

This is a valid Theorem-1.2 boundary request:

\[
 D=B\cap C,\qquad D\ne M,\qquad
 D\ne\mu^{-1}(C)=02.                                      \tag{4.5}
\]

Nevertheless no directed Hamilton path runs from `C` to `B`.  The failure
has a short forced-arc certificate.  Number the owners in the order shown
in (4.1), so `C=T_5` and `B=T_4`.  The root-link arcs are

\[
\begin{array}{c|c@{\qquad}c|c}
0&3,6&1&3,8\\
2&1,7&3&2,9\\
4&0,1&5&0,2\\
6&4,8&7&4,5\\
8&7,9&9&5,6.
\end{array}                                                \tag{4.6}
\]

Because `5` is the start, `7->5` and `9->5` are forbidden; therefore
`7->4` and `9->6` are forced.  Because `4` is the end, `4->0` and `4->1`
are forbidden; hence `5->0` and `2->1` are forced.  Now `2->1` forces
`8->7`, which forces `3->9`.  But the only remaining predecessor of `2` is
also `3`, forcing `3->2`, a contradiction.

Thus the endpoint-universal claim is false for a purely topological reason;
upper coverage never gets a chance to fail.

## 5. Exhaustive audit and provenance

The audit enumerates the `3^10` possible choices in (1.1), retains exactly
the choices with ten distinct roots, and then depth-first enumerates every
directed Hamilton path of (1.2).  For every path it records its ordered
endpoints and the five-bit rank-four union palette.  It separately enumerates
every tuple `(M,B,D,C)` satisfying the fixed-boundary conditions.

Authoritative H100 root:

```text
/home/amodo/or15/work/root_small_mu_upper_census_20260802
```

Artifacts:

```text
scratch/audit_small_mu_upper_census_20260802.cpp
  SHA256 ea4bb533729c462c11fd4fcd0ed08bb2cce0b8faa7a2b0d2e509d8f69944091b

H100 O3 binary
  SHA256 d7c958110a29cc673740c12185e9bbcfc7c5ca275c06bc0f4bd60d408e698c1b

scratch/audit_small_mu_upper_census_20260802.out
  SHA256 f97ed63af39f2aa9cba5a1d000f952be00476479b68d9c2719d2581e50ede80e
```

Key output:

```text
matchings=60
matchings_with_hamilton=60
matchings_with_upper_hamilton=60
hamilton_paths=2280
upper_hamilton_paths=2280
all_endpoint_requests=5400 plain=1740 upper=1740
relevant_endpoint_requests=1200 plain=600 upper=600
petersen_cycle_type_histogram: 2+2+2+2+2:6 2+8:30 5+5:24
digest_fnv64=0x8f50ec90b5b0f8fb
```

## 6. Scope

This closes the requested `K5` census.  It proves neither that every
matching has a Hamilton root-link path for larger `r`, nor that upper
surjectivity remains automatic.  Its constructive guidance is precise:

\[
 \boxed{\text{select the containment matching and protected boundary jointly.}}
\]

At the smallest nontrivial case, the `5+5` Petersen class is the robust
choice; the five-transposition class is maximally hostile to the lollipop
endpoint condition.
