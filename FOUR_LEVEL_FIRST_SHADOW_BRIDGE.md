# A four-level Hamilton-cycle bridge to an exact two-sided first shadow

## 1. Statement

Fix `m>=2`.  Let `R` be a ground set of size `2m-1`, and let `z` be one
additional coordinate.  Put

\[
 p={2m-1\choose m-1}={2m-1\choose m},\qquad
 q={2m-1\choose m-2}={2m-1\choose m+1},
\]

and

\[
 b=p-q=\frac1{m+1}{2m\choose m}=\operatorname{Cat}_m.
\tag{1.1}
\]

Consider a Hamilton cycle `H` in the subgraph of the Boolean cube on `R`
induced by ranks

\[
                    m-2,m-1,m,m+1.                 \tag{1.2}
\]

Such a Hamilton cycle is known to exist, but the extra hypotheses below are
not automatic.

For a rank-`(m-2)` vertex `C`, let `Y_C,Y'_C` be its two neighbours on `H`
and define its upper square completion

\[
                    \psi(C)=Y_C\cup Y'_C\in{R\choose m}.       \tag{1.3}
\]

For a rank-`(m+1)` vertex `D`, let `X_D,X'_D` be its two neighbours and
define its lower square completion

\[
                    \phi(D)=X_D\cap X'_D\in{R\choose m-1}.     \tag{1.4}
\]

Assume:

1. `psi` is injective;
2. `phi` is injective; and
3. if
   \[
    P={R\choose m-1}\setminus\phi\left({R\choose m+1}\right),
    \qquad
    Q={R\choose m}\setminus\psi\left({R\choose m-2}\right),   \tag{1.5}
   \]
   then the central edges of `H` between ranks `m-1` and `m` contain a
   perfect matching from `P` to `Q`.

### Theorem 1 (square-resolved four-level bridge)

Under these hypotheses there is a collection `E` of

\[
                         {2m\choose m-1}             \tag{1.6}
\]

Johnson edges on the middle layer `binom(R+z,m)` such that

* every rank-`(m-1)` set is the meet of exactly one edge of `E`;
* every rank-`(m+1)` set is the join of exactly one edge of `E`; and
* the graph formed by `E` is a spanning union of exactly `Cat_m` paths.

Thus a square-resolved four-level Hamilton cycle would give an exact
two-sided first-shadow path factor on the next even cube.

This theorem does **not** assert that the known four-level Hamilton cycle has
the three square-resolution properties, and it does not by itself control
coordinate runs, complementary endpoints, path lengths, or deeper shadows.

## 2. Suppressing the two outer levels

Every outer vertex of `H` has both neighbours in the same inner level.  Replace
each two-edge subpath through a rank-`(m-2)` or rank-`(m+1)` vertex by an edge
between its two neighbours.  The result is a Hamilton cycle `G` on the `2p`
vertices in ranks `m-1` and `m`.

There are `q` suppressed edges internal to rank `m-1`, `q` suppressed edges
internal to rank `m`, and all remaining edges of `G` are the central edges of
`H`.  Counting degrees at the outer levels shows that their number is

\[
 2(p+q)-4q=2(p-q)=2b.                               \tag{2.1}
\]

Map the inner vertices into the middle layer of the `2m`-cube by

\[
       Y\in{R\choose m-1}\longmapsto Y+z,
       \qquad
       X\in{R\choose m}\longmapsto X.               \tag{2.2}
\]

This is a bijection onto `binom(R+z,m)`, so `G` is now a Hamilton cycle on
the entire middle layer of the enlarged cube.

## 3. The colors of the three edge types

The suppressed edge through `C in binom(R,m-2)` joins `Y_C+z` to
`Y'_C+z`.  Its meet and join are

\[
                    C+z,\qquad \psi(C)+z.             \tag{3.1}
\]

The suppressed edge through `D in binom(R,m+1)` joins `X_D` to `X'_D`.
Its meet and join are

\[
                    \phi(D),\qquad D.                 \tag{3.2}
\]

Finally, a central cube edge `Y subset X` becomes the Johnson edge
`Y+z -- X`, whose meet and join are

\[
                    Y,\qquad X+z.                      \tag{3.3}
\]

Consequently the lower suppressed edges cover every meet containing `z`, and
the upper suppressed edges cover every join avoiding `z`, each exactly once.
Injectivity of `phi` and `psi` says that their other colors have no collision.
The only missing colors are precisely the two residual sets `P,Q` from
(1.5), both of size

\[
                         p-q=b.                        \tag{3.4}
\]

The matching in hypothesis 3 covers those residual colors exactly by (3.3).
This proves the two rainbow assertions.

## 4. Why the selected edges are paths

Keep every suppressed edge of `G` and the `b` central edges in the matching
from hypothesis 3.  Equation (2.1) shows that exactly `b` central edges of
the Hamilton cycle `G` are deleted.  Deleting `b>=1` distinct edges from one
cycle leaves exactly `b` spanning path components.

The selected-edge count is

\[
 2q+b=p+q={2m\choose m-1},                           \tag{4.1}
\]

which also agrees with the number of colors on either adjacent layer.  This
finishes the proof of Theorem 1.

## 5. Exact next question

The recent theorem that the middle four levels of every odd cube have a
Hamilton cycle supplies `H` but not visibly (1.3)--(1.5).  The sharply posed
first test is therefore:

> Does the lexical four-level Hamilton cycle admit local cycle switches which
> make both square-completion maps injective and leave a perfect matching on
> the two residual central vertex sets?

Even a version with `o(p)` completion collisions and `o(p)` unmatched
residual vertices would yield an asymptotically lossless first-shadow path
factor.  Extending that factor through growing depth would still be a separate
problem.
