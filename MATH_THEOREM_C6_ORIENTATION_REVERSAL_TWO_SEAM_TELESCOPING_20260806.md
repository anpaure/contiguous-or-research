# Orientation reversal telescopes two upper-value seams along a C6 connector path

## Status

The literal three-way C6 splice preserves every owner and root occurrence,
but its shortest private-token collar leaves two immediate-upper cells at
each of its three cuts outside the protected tensor.  Six fresh backup
obligations per port exceed the total upper surplus for a spanning loose
path of near-maximal antipodal rings.

This note proves the missing constant-efficiency identity at the level at
which it is currently justified.  Reverse the cyclic orientation of the
three active labels at the next port and carry the two far tokens on the
shared component according to the displayed index map.  The two new
extreme-upper **values** at the old shared cut are then exactly the two old
extreme-upper values at the next shared cut.  They cancel in the signed
target-multiplicity ledger.

Equality of the values does not by itself identify their physical
occurrence tickets.  Literal occurrence transport requires the output
cell of the preceding port to be the input cell of the following port (or
an explicit typed occurrence bijection).  Conditional on a valid serial
realization, value equality is nevertheless sufficient for the exact
final upper-coverage count, because that count depends only on the net
multiplicity of each upper target.

Consequently a valid loose path of `m` ports has at most `4m+2` uncancelled
negative upper-occurrence terms, rather than `6m`.  The number of actually
missing upper targets is at most this quantity and can be smaller.  For
periods near `q+h-1`, the exact upper surplus `2W_q/(q+1)` is at least this
scalar ceiling.  What remains is an incidence-level matching into free
duplicate-provider tickets and a literal regeneration theorem for the
shared hub state.

## 1. One port's two extreme cells at a cut

Use the cyclic index set `Z/3Z`.  At cut `t`, write the two old extreme
upper values in the form

\[
 \begin{aligned}
 E_t^R&=B^R\cup\{a_t,a_{t+1},x_t\},\\
 E_t^L&=B^L\cup\{a_t,a_{t+1},y_t\},
 \end{aligned}                                          \tag{1.1}
\]

where `B^R,B^L` contain the corresponding common full filler profiles and
none of the displayed active or far labels.  Under the cyclic tail splice
`left(t)->right(t+1)`, the two new values at the same left-indexed cut are

\[
 \begin{aligned}
 N_t^R&=B^R\cup\{a_t,a_{t+2},x_{t+1}\},\\
 N_t^L&=B^L\cup\{a_t,a_{t+2},y_t\}.
 \end{aligned}                                          \tag{1.2}
\]

These are precisely the two addresses `(1,h)` and `(h,1)` omitted by the
`(h-1)`-collar C6 tensor.  Formula (1.2) follows by attaching the right
collar of component `t+1` while retaining the left collar of component
`t`.

## 2. Exact orientation-reversal identity

Define the next port's active orientation and shared far tokens by

\[
 b_s=a_{-s},
 \qquad
 x'_s=x_{1-s},
 \qquad
 y'_s=y_{-s}.                                            \tag{2.1}
\]

Use the same two common bases `B^R,B^L` on the shared hub cut.

### Theorem 2.1 (two-seam regeneration)

For every `t`, put `s=-t`.  The next port's two old extreme values at cut
`s` are exactly the preceding port's two new values at cut `t`:

\[
 \boxed{
 E_s^{\prime R}=N_t^R,
 \qquad
 E_s^{\prime L}=N_t^L.}                                 \tag{2.2}
\]

#### Proof

The next old active pair at index `s=-t` is

\[
 \{b_s,b_{s+1}\}
   =\{a_t,a_{t-1}\}
   =\{a_t,a_{t+2}\}.                                    \tag{2.3}
\]

Also

\[
 x'_s=x_{1+t}=x_{t+1},
 \qquad y'_s=y_t.                                       \tag{2.4}
\]

Substituting (2.3)--(2.4) in (1.1) for the primed port gives (1.2)
verbatim. \(\square\)

The map (2.1) is involutive: applying it twice restores the original active
orientation and both far-token triples.  Thus successive ports may
alternate between two exact boundary types.

### Corollary 2.2 (the whole shared collar regenerates)

Suppose the protected part of the old port has cumulative profiles

\[
 L_i^{(t)}=\Lambda_i\cup\{a_t\},
 \qquad
 R_j^{(t)}=P_j\cup\{a_{t+1}\}
 \qquad(1\le i,j\le h-1).                               \tag{2.5}
\]

After the splice `left(t)->right(t+1)`, its new seam has profiles

\[
 \Lambda_i\cup\{a_t\},
 \qquad
 P_j\cup\{a_{t+2}\}.                                   \tag{2.6}
\]

At the next-port index `s=-t`, these are exactly

\[
 \Lambda_i\cup\{b_s\},
 \qquad
 P_j\cup\{b_{s+1}\}.                                   \tag{2.7}
\]

Hence the complete protected old C6 collar, not only its two extreme upper
sets, regenerates with reversed orientation.  Every local ticket transported
by the first splice is already at the correct address for the next splice.

#### Proof

The first identity in (2.7) is `b_(-t)=a_t`.  The second is

\[
 b_{-t+1}=a_{-(-t+1)}=a_{t-1}=a_{t+2}.
\]

Substitute in (2.5)--(2.6). \(\square\)

This is a literal local regeneration statement.  Reusing it through many
fresh components still requires the common profiles and repeated active
coordinates to be globally resource-disjoint away from the intentionally
shared seam and to satisfy their final capped run/gap ages.

## 3. Telescoping along a loose path

Consider a serial loose connector path of `m` C6 ports.  Consecutive ports
share one current component.  Require the output cut of port `i` and the
input cut of port `i+1` to obey Theorem 2.1; the other two input cuts of
port `i+1` lie in its two fresh components.

### Theorem 3.1 (conditional four-current value ledger)

Assume that all `m` ports have a simultaneous or serial literal
realization, so their displayed old and new extreme cells are the actual
destroyed and created occurrences of one physical chronology.  In the
signed immediate-upper **target-value** ledger, the two output seam values
on every internal shared cut cancel exactly with the two input seam values
of the next port.  Therefore the number of uncancelled negative extreme
occurrence terms is at most

\[
                         6+4(m-1)=4m+2.                  \tag{3.1}

\]

All cancellations preserve the target value and the left/right typed role.
They preserve occurrence-labelled tickets only under the additional
shared-ticket identification stated below.

#### Proof

Port one has six old extreme cells.  Every later port has six.  By (2.2),
the values of its two negative terms on the shared component equal the
values of the two positive terms just created by the preceding port.  In
the free abelian group on typed upper-target values, those terms cancel.
The remaining four negative terms lie on the two fresh components.  This
gives (3.1). \(\square\)

For actual occurrence-ticket cancellation one needs a bijection

\[
 \theta_i:C_i^{\rm shared}\longrightarrow L_{i+1}^{\rm shared}
                                                               \tag{3.2}
\]

from the two created shared cells of port `i` to the two destroyed shared
cells of port `i+1`, preserving the physical cell (or accepted typed ticket
name), side, cap state, and occurrence guards.  Equations (2.2) and
Corollary 2.2 prove equality of the complete local set-valued profiles;
they do not on their own prove that the two profiles are planted on the
same physical tickets in a global chronology.

If the cells are distinct but all ports are otherwise literally valid,
the value-level cancellation still gives the correct final multiplicity:
one occurrence of a target is created and one is destroyed.  Such a pair
cannot, however, be treated as a transported occurrence in any other
owner, root, lower-ticket, or common-cap ledger.

Corollary 2.2 supplies the reversed shared collar after the preceding
fusion.  A physical serial realization must still plant it on compatible
occurrence tickets, plant the other two fresh collars without collisions,
and pass the final capped-age tests.

## 4. Exact comparison with the global upper surplus

Let

\[
                         L=q+h-1,                        \tag{4.1}

\]

and schedule `c` long rings of periods `L-1,L` whose lengths sum to
`W_q`.  Then

\[
                         c\le {W_q\over L-1}.             \tag{4.2}

\]

A loose path uses

\[
                         m=\left\lfloor{c-1\over2}\right\rfloor,
 \qquad
                         4m+2\le2c.                      \tag{4.3}

\]

The exact upper surplus is

\[
                         E_U={2W_q\over q+1}.             \tag{4.4}

\]

If `h>=3`, then `L-1=q+h-2>=q+1`, and therefore

\[
 \boxed{
                         4m+2
                    \le {2W_q\over L-1}
                    \le {2W_q\over q+1}=E_U.}           \tag{4.5}

\]

Thus the unavoidable upper duplicate budget is scalarly at least the
number of uncancelled negative seam terms in the orientation-alternating
loose path.  This is a necessary capacity comparison only.  It does not
say that the surplus occurrences have the required target values or are
free under the other typed ledgers.  No scalar `3/2` deficit remains.

## 5. Exact residual multiplicity and the provider Hall graph

Let `mathcal U` be the immediate-upper target set.  Before the connector
path is applied, let

\[
                         \mu_0(U)                       \tag{5.1}
\]

be the number of physical occurrences of `U`.  Let `ell(U)` and `n(U)` be
the numbers of actual destroyed and created upper occurrences of value
`U` in the complete serial path.  Then the final multiplicity is exactly

\[
              \mu_f(U)=\mu_0(U)-\ell(U)+n(U).           \tag{5.2}
\]

The value identities (2.2) cancel one summand of `ell` with one summand of
`n` on each internal shared cut, whether or not the two tickets are
physically identical.  Hence

\[
 \sum_{U\in\mathcal U}\bigl(\ell(U)-n(U)\bigr)_+
                         \le 4m+2.                      \tag{5.3}
\]

The actual missing-target set is

\[
              \mathcal D=\{U\in\mathcal U:\mu_f(U)=0\} \tag{5.4}
\]

and therefore

\[
                         |\mathcal D|\le4m+2.            \tag{5.5}
\]

In particular, `4m+2` counts neither necessarily distinct targets nor
automatically available provider tickets.

To state the remaining integral gate, expose a set `mathcal P` of free
physical surplus-provider tickets.  This must be a **capacity-faithful**
surplus bank: if its tickets are currently providers of a target `V`, at
most the number of copies of `V` which may be removed while leaving one
protected final copy are admitted to `mathcal P`.  Thus choosing several
right vertices cannot silently consume the last copy of a donor target.
A right vertex is a complete typed ticket, not merely an abstract unit of
the scalar surplus: it records its physical occurrence, current donor
value, phase, side, cap state, and every protected resource which its use
consumes.  Define the bipartite graph

\[
 H_{\rm prov}\subseteq\mathcal D\times\mathcal P        \tag{5.6}
\]

by joining `U` to `p` precisely when ticket `p` can be retained or coloured
as an occurrence of `U` while respecting the fixed owner/root factor,
residence, lower tickets, and cap guards.  If all remaining conflicts are
exactly the unit capacities of the right vertices, then the seam targets
have distinct backup providers if and only if

\[
 \boxed{
 |N_{H_{\rm prov}}(X)|\ge |X|
 \quad\hbox{for every }X\subseteq\mathcal D.}           \tag{5.7}
\]

This is the exact provider Hall row.  If two nominal provider tickets have
an additional shared resource not encoded in their right vertex, ordinary
Hall is not sufficient; the right side must first be refined into complete
resource packets, or the problem must be treated as the corresponding
matching-with-conflicts system.

For an initially upper-complete factor with `N` occurrences on a bank of
`M` targets, the total duplicate excess is

\[
                 \sum_U(\mu_0(U)-1)=N-M=E_U.            \tag{5.8}
\]

Only the unprotected part of this excess belongs to `mathcal P`.  Thus
(4.5) proves merely that the cardinality obstruction can be met in the
best case:

\[
              |\mathcal D|\le4m+2\le E_U.               \tag{5.9}
\]

It does not prove `|mathcal P|=E_U`, and even that equality would not imply
the Hall inequalities (5.7).

## 6. Revised exact remaining rows

The upper seam problem has split into two sharply stated integral tasks.

1. **Regenerative planting.**  Corollary 2.2 gives the literal reversed
   hub collar.  Plant it on compatible occurrence tickets, plant the other
   two fresh collars without owner/root/ticket collisions, and space all
   reused profile and active coordinates so the final capped ages are
   legal.  If another ledger needs occurrence transport, prove (3.2).
2. **Duplicate-provider Hall.**  Choose the original coloured ring factor
   and its free provider tickets so that the capacity-faithful graph
   `H_prov` satisfies (5.7), without consuming protected owner/root or
   lower-ticket resources.

The first is a literal regenerative port theorem; the second is a
capacity-faithful occurrence matching.  The scalar upper-current
obstruction, including its formerly wrong factor `3/2`, is closed by
Theorems 3.1--4.5.  Exact occurrence transport and provider Hall remain
open.
