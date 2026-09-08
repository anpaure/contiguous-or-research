# Full prefix/suffix signatures make local replacements transparent at every width

Date: 2026-07-31  
Status: exact word lemma and composition theorem.  This removes
arbitrary-width upper-witness bookkeeping **if** the packet catalogue can be
made signature-preserving.  Uniform existence of such buffered C6/ECO
packets is open.

## 1. The signature

For a nonempty word fragment

\[
                        X=(X_1,\ldots,X_\ell)
\]

of subsets of one ground set, define its ordered boundary signature

\[
 \Sigma(X)=\left(
   \left(\bigcup_{i=1}^jX_i\right)_{1\le j\le\ell},
   \left(\bigcup_{i=j}^{\ell}X_i\right)_{1\le j\le\ell}
            \right).                                      \tag{1.1}
\]

The two coordinates are pointwise prefix and suffix unions.  Equality as
unordered multisets is not enough.

For a coordinate `x`, write

\[
 \operatorname{first}_X(x)=\min\{i:x\in X_i\},\qquad
 \operatorname{last}_X(x)=\max\{i:x\in X_i\},             \tag{1.2}
\]

with the values `+infinity,-infinity` when `x` is absent.

### Lemma 1.1 (endpoint-time characterization)

For equal-length fragments `X,Y`,

\[
 \boxed{\Sigma(X)=\Sigma(Y)
 \iff
 \bigl(\operatorname{first}_X(x),\operatorname{last}_X(x)\bigr)
 =
 \bigl(\operatorname{first}_Y(x),\operatorname{last}_Y(x)\bigr)
 \quad\text{for every }x.}                                  \tag{1.3}
\]

#### Proof

A coordinate belongs to the `j`th prefix union exactly when its first
occurrence is at most `j`.  Thus equality of every prefix union is equivalent
to equality of all first-occurrence positions.  Dually, a coordinate belongs
to the suffix beginning at `j` exactly when its last occurrence is at least
`j`; equality of all suffix unions is equivalent to equality of all last
positions.  Combine the two statements. \(\square\)

This is the useful packet form of the signature.  Interior occurrences may
be changed arbitrarily; only the entry and exit time of each coordinate must
be preserved.  In particular, resident rails are naturally suited to this
interface: they may reroute a coordinate inside a packet while keeping its
two boundary times fixed.

For simultaneous upper unions and lower intersections, apply the same
definition to complements and put

\[
                         \Sigma^{\pm}(X)
                    =\bigl(\Sigma(X),\Sigma(\overline X)\bigr). \tag{1.4}
\]

Equality of `Sigma^plusminus` says that every coordinate has the same first
and last occurrence **and** the same first and last absence in the two
fragments.  By De Morgan, it preserves every crossing intersection as well
as every crossing union.  A construction which repairs lower rows through a
separate compiler needs only the union half; a packet advertised as
all-depth upper/lower transparent needs the full signature (1.4).

## 2. Exact local replacement theorem

### Theorem 2.1 (all-width transparency)

Let

\[
             A=P\,X\,S,\qquad A'=P\,Y\,S,
\]

where `X` and `Y` have the same length.  If

\[
                              \Sigma(X)=\Sigma(Y),          \tag{2.1}
\]

then every interval of `A` which is not contained wholly inside `X` has the
same union as the corresponding interval of `A'`.  The analogous statement
holds with `X` and `Y` interchanged.

Consequently the only interval-union targets which can be lost or created
by the replacement are represented by intervals wholly inside the replaced
fragment.

#### Proof

Intervals disjoint from the replaced positions are unchanged.  An interval
which crosses only the left boundary is the union of an unchanged suffix of
`P` and one prefix union of `X`; use the first coordinate of (2.1).  An
interval which crosses only the right boundary is one suffix union of `X`
plus an unchanged prefix of `S`; use the second coordinate.  An interval
which crosses both boundaries contains all of `X`, whose union agrees with
that of `Y` by either coordinate of (2.1).  These exhaust all intervals.
\(\square\)

The conclusion is literal, not merely a preservation of coverage.  Every
crossing interval retains exactly its old value at exactly its old address.

### Corollary 2.2 (carrier-window form)

The same theorem applies when the letters are middle owners in a carrier
chronology.  Thus a signature-preserving owner-fragment replacement preserves
every consecutive-owner union crossing its boundary, simultaneously at all
depths.  Only consecutive unions internal to the packet require a local
palette certificate.

In particular, a packet of length `O(d(k))` has physical crossing dependency
span `O(d(k))`, even though the ambient word has upper windows of length
`Theta(k)`.  This statement concerns the crossing boundary.  The packet
still has `Theta(d(k)^2)` internal intervals, and they cannot silently be
replaced by `O(d(k))` independent semantic constraints.

For a fragment `X`, write

\[
 \mathcal U(X)=
 \left\{\bigcup_{t=i}^jX_t:1\le i\le j\le\ell\right\}.       \tag{2.2}
\]

### Corollary 2.3 (signature plus internal dominance)

Under the hypotheses of Theorem 2.1, if additionally

\[
                         \mathcal U(X)\subseteq\mathcal U(Y),  \tag{2.3}
\]

then every interval-union value occurring anywhere in the old word `PXS`
still occurs in the new word `PYS`.

#### Proof

Theorem 2.1 preserves every noninternal interval at the same address.
Equation (2.3) recreates every internal old value inside `Y`. \(\square\)

Thus all `Theta(d^2)` internal checks may be discharged as one **unary local
packet certificate** instead of being exported as shared conflict tokens.
For a reversible cube, use equality
`mathcal U(X)=mathcal U(Y)`; for a one-way repair, the inclusion (2.3) is
enough because overcoverage is free.

## 3. Composition

### Theorem 3.1 (disjoint transparent packets compose)

Let `X_1,...,X_t` be pairwise position-disjoint fragments of a word.  For
each `i`, replace `X_i` by an equal-length `Y_i` with

\[
                              \Sigma(X_i)=\Sigma(Y_i).
\]

Then every interval not contained wholly in one of the packet supports has
the same union before and after all replacements.

If every replacement also satisfies the one-way internal dominance
`mathcal U(X_i) subseteq mathcal U(Y_i)`, then the final word retains every
old interval-union value.  If equality holds for every packet, every subset
state has exactly the same union-value support outside any separately
declared local payload.

#### Proof

Apply Theorem 2.1 one replacement at a time.  At each step every interval
not internal to the currently replaced fragment is unchanged.  An interval
crossing several packet supports is therefore unchanged at every step.
Pairwise position-disjointness keeps all later fragment addresses fixed.
\(\square\)

This composition theorem removes the three-packet witness failure in which
different packets destroy the last three occurrences of one target.  No
protected global witness bank is needed for crossing intervals: their
literal values are invariant packet by packet.

Internal packet intervals must still be certified jointly with the local
owner, residence, lower-palette and common-cap rows.

## 4. Why weaker boundary data do not suffice

Equality of the total union, the first and last letters, or a bounded number
of endpoint types does not imply Theorem 2.1.  For example,

\[
 X=(\{a\},\{b\},\{c\}),\qquad
 Y=(\{a\},\{b,c\},\{c\})
\]

have the same first letter, last letter and total union, but the length-two
prefix unions are respectively `{a,b}` and `{a,b,c}`.  An interval entering
from the left and ending at the second packet position therefore changes.

Hence the phrase “boundary-equivalent” in a packet theorem must explicitly
include (2.1), or an independently proved weaker signature which still
determines every crossing union.

## 5. Exact construction target for buffered C6/ECO packets

The upper-compression gate can now be stated without asymptotic language.
For every eligible repair task, construct `Omega(m^2)` old/new packet pairs

\[
                          X_{b,c}\longleftrightarrow Y_{b,c}
\]

such that:

1. `|X_(b,c)|=|Y_(b,c)|=O(d(k))`;
2. `Sigma(X_(b,c))=Sigma(Y_(b,c))` pointwise;
3. the internal union-value bank satisfies
   `mathcal U(X_(b,c)) subseteq mathcal U(Y_(b,c))`, or a declared payload
   version of this inclusion;
4. residence, physical topology and the complete common-cap ticket are
   valid on both phases; and
5. after all guards, at most `O(md(k))` of the `(b,c)` pairs are rejected,
   preferably through the proved bad-pair star-cover criterion.

If this target holds and the internal dominance check is treated as unary
packet validity rather than `Theta(d^2)` shared resources, arbitrary-width
upper shadows no longer force the physical dependency parameter
`D_m=Theta(m)` in the sparse-exposure theorem.  One may take

\[
                              D_m=O(d(k))=O(\sqrt m),
\]

which restores the asymptotic list-versus-conflict gap

\[
                        m^2\gg mD_m.
\]

The theorem above proves this implication.  It does not prove that the
incidence C6, suspended hexagon, or all-six ECO catalogue has the required
signature.  That is now a finite local algebra problem on the proposed
buffered fragments, rather than an all-depth global witness problem.
