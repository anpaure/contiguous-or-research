# Audit of the unbuffered alternating primitive reservoir

Date: 2026-08-02  
Status: independent proof audit.  The shortest proposed packet is accepted
through the owner row and refuted at immediate upper rank in even parity.
The one-pair parity correction is accepted, including clustered pruning and
aggregate reservation.  Global component fusion remains open.

## 1. Object audited

Put

\[
 q=d+2,\qquad c=r-q+1,\qquad W=\binom{k}{r}.
\]

For a `(c-1)`-core `X`, a refreshed point `beta`, and cyclic private tags
`z_0,...,z_(L-1)`, consider

\[
 S_t=\begin{cases}
 X\cup\{z_t\},&t\text{ even},\\
 X\cup\{\beta,z_t\},&t\text{ odd}.
 \end{cases}                                             \tag{1.1}
\]

The conjectured shortest choice is

\[
 m_0=\left\lceil q/2\right\rceil,\qquad L_0=2m_0.
                                                               \tag{1.2}
\]

The corrected full immediate-upper choice is

\[
 m=\left\lfloor q/2\right\rfloor+1,\qquad
 L=2m=\begin{cases}q+2,&q\text{ even},\\q+1,&q\text{ odd}.
 \end{cases}                                                \tag{1.3}
\]

## 2. Exact parity verdict

Every union of `j>=2` consecutive sources in (1.1) is

\[
                  X\cup\{\beta\}\cup J,
\]

where `J` is the corresponding cyclic `j`-interval of private tags.  In
particular an owner uses `j=q-1` and has rank

\[
                 (c-1)+1+(q-1)=r.                         \tag{2.1}
\]

For the shortest choice (1.2), all marked lower intervals have lengths at
most `q-2` and owners have length `q-1<L_0`; their starts are therefore
distinct in both parities.  Hence the literal cycle, marked lower deck, and
owner deck are valid.

The immediate-upper value at an edge is the union of two consecutive
owners, hence uses a cyclic `q`-interval.  If `q` is odd, `L_0=q+1`, so
these are the distinct complements of one private tag.  If `q` is even,
`L_0=q` and every such interval is the full tag set.  More explicitly,

\[
 O_i=X\cup\{\beta\}\cup(V-\{z_i\}),\qquad
 O_i\cup O_{i+1}=X\cup\{\beta\}\cup V.                  \tag{2.2}
\]

Thus the proposed minimal packet has immediate-upper support one in even
parity.  This is a literal equality obstruction, not a counting or
matching defect.  Because an alternating packet has even length, the next
possible length is `q+2`; (1.3) is therefore the minimal uniform correction.
With `L>q`, all cyclic intervals used through immediate upper rank are
proper and have distinct starts.

## 3. Rank and footprint audit of the corrected packet

The complete audited rows and multiplicities are

\[
\begin{array}{c|c}
\text{rank}&\text{count}\\ \hline
c&m\\
c+1&m\\
c+j,\ 2\le j\le q-2&L\\
r&L\\
r+1&L.
\end{array}                                               \tag{3.1}
\]

There are `q-3` intermediate high ranks.  Therefore the total typed
footprint count is

\[
             2m+L(q-3)+L+L=Lq=\Theta(q^2).               \tag{3.2}
\]

Each cycle realizes exactly `m` copies of
`g_(d-1,d+1)=e_(d-1)+e_(d+1)` and uses no short-buffer occurrence.

## 4. Fixed-support trace and clustered pruning

Fix `A={beta} dotcup V`, `Q=|A|=L+1`, and let

\[
             X\in\binom{[k]-A}{c-1},\qquad
             M_L=\binom{k-Q}{c-1}.
\]

Every named resource is `X dotcup R` with `R subseteq A`; hence its outside
trace recovers `X`.  The exact reservoir-to-owner ratio is

\[
 {M_L\over W}=
 { (r)_q (k-r)_{Q-q}\over(k)_Q}
 =2^{-Q}\exp(O(q^2/k))=\Theta(2^{-q})                    \tag{4.1}
\]

in the canonical central range.

For a second support `A'`, put `E=A'-A`.  Equality with one fixed typed
second footprint forces the single trace equation

\[
                         X\cap E=R'\cap E.                \tag{4.2}
\]

Consequently one opposing packet contributes only `Lq`, not `(Lq)^2`,
trace cylinders.  A prescribed trace has relative mass at most
`C2^{-|E|}`.  Averaging over random supports uses

\[
          \mathbb E 2^{|A\cap A'|}
          \le \exp\!\left({Q^2\over k-Q+1}\right)=O(1),  \tag{4.3}
\]

and gives mean damage `O(M_L q^2/2^q)` per ordered reservoir pair.  Sampling
`Theta(2^q/q^2)` supports and deleting every colliding module therefore
retains

\[
                         \Omega(W/q^2)                    \tag{4.4}
\]

pairwise owner/lower/immediate-upper named-deck-disjoint literal cycles.
They contain `Omega(W/q)` primitive copies.

The same expectation with a preused bank gives exactly the weighted load

\[
 m\frac{|D_c|}{\binom{k}{c}}+m\frac{|D_{c+1}|}{\binom{k}{c+1}}
 +L\sum_{j=2}^{q-2}\frac{|D_{c+j}|}{\binom{k}{c+j}}
 +L\frac{|D_r|}{W}+L\frac{|D_{r+1}|}{\binom{k}{r+1}}.    \tag{4.5}
\]

In particular, the last term is mandatory for the corrected q1 statement;
it is absent from the shortest lower/owner-only theorem.

## 5. Aggregate reservation audit

Reserving `t` corrected cycles subtracts

\[
                     tm e_{d-1}+tm e_{d+1}.               \tag{5.1}
\]

The low and high resource totals fall equally, so `L_low-H_high` is
unchanged.  If the four conductor coordinates remain at least `Q_(r,d)+1`,
the exact rotor-semigroup theorem applies to the residual vector.  Since
the canonical two changed coordinates are `Theta(W/q)`, while
`m=Theta(q)` and the conductor is `o(W/q)`, a sufficiently small constant
multiple of `W/q^2` cycles can be reserved.  This verifies that the
unbuffered packet removes the scalar short-buffer obstruction, including
the `L_low-H_high=0` face.  It does not name or chronologize the residual
semigroup decomposition.

## 6. Chronology obstruction after packing

For a source word `S`, let

\[
 \mathbf U_t(S)=
 (S_t,S_{t-1}\cup S_t,\ldots,\bigcup_{i=0}^{d}S_{t-i}). \tag{6.1}
\]

For a two-cycle cut and cross-reconnection, equality of the old and new
affected marked-chain multisets is an exact sufficient transport
certificate.  It is necessary only when those complete chain signatures
are themselves unique protected resources; it is not necessary for every
weaker selected-row protection policy.

There is a simpler necessary rank test.  If a new owner window mixes
packets with `(c-1)`-cores `X,Y`, then it contains `X union Y`.  Since
`|X|=|Y|=r-q`, a rank-`r` owner requires

\[
             |X\setminus Y|=|Y\setminus X|\le q.       \tag{6.2}
\]

The clustered-pruning argument neither selects such nearby cores nor
provides chain-transparent sockets among them.  Thus it proves local source
chronologies and named-resource capacity, but not a global connected
chronology.  Exterior cross-windows, residence after joins, arbitrary deep
upper shadows, and common-cap/compiler feasibility remain separate gates.

### Relation to cyclic quotient development

The quotient theorem says that developing a base cycle under a free cyclic
action is resource-simple exactly when its typed deck is internally
orbit-simple and the chosen quotient decks are disjoint.  The present
clustered-pruning theorem does not assert that orbit condition: it samples
ordinary coordinate supports and deletes literal collisions.  Hence one
cannot multiply (4.4) by a group order or infer an equivariant chronology.

Conversely, the authenticated `k=17` `Z_17` bank consists of buffered
one-primitive modules, whereas (1.1) is an unbuffered multi-primitive cycle.
At `k=17`, `q=5` is odd, so the local parity collapse does not occur, but
neither the asymptotic extraction nor the finite quotient certificate binds
these new cycles to a protected host.  The two results are compatible and
solve different rows: quotient development gives a finite symmetric named
bank; clustered pruning gives an all-large-`k`, generally asymmetric named
bank.

## 7. Verdict

The proposed extension is not valid verbatim if “named deck” includes the
immediate-upper row: even `q` has the exact collapse (2.2).  It is valid
verbatim through the owner row.  Adding one `PH` pair only in even parity
repairs the q1 row and preserves the claimed asymptotic packing and
aggregate-reservation scales.  No parity, rank, or trace obstruction remains
for that corrected local theorem.  The first unresolved physical theorem is
component fusion through protected chain-transparent sockets or an ambient
host supplying duplicate crossing witnesses.

The audited theorem is
`MATH_THEOREM_FACET_UNBUFFERED_MULTIPRIMITIVE_CLUSTERED_PRUNING_AND_SOCKET_RESERVATION_20260802.md`.
Its clustered-pruning dependency is
`MATH_THEOREM_FACET_FIXED_BASE_COLLISION_TENSOR_AND_WHOLE_FRAME_NOGO_20260802.md`;
its local-cycle dependency is
`MATH_THEOREM_R_PRIMITIVE_MIXED_ROTOR_SHARP_BUFFERED_ONE_COPY_LIFT_20260801.md`;
and its exact residual dependency is
`MATH_THEOREM_AGGREGATE_MONOTONE_ROTOR_SEMIGROUP_AND_BUFFER_ROUNDING_20260801.md`.
