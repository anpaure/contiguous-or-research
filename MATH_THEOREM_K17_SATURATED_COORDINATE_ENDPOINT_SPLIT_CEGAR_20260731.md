# K17 saturated-coordinate endpoint rigidity and exact marked-sector CEGAR

Date: 2026-07-31  
Status: solver-free fixed-parent saturated-fibre no-go and exact restricted
model; no unrestricted K17 no-go

## 1. Scope and authenticated inputs

Let

~~~text
X = scratch/k16_optimal_12873_20260731.word
SHA-256 890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe
~~~

be the authenticated optimal K16 word, of length \(n=12873\). Let \(z\)
be a seventeenth coordinate. This note studies only words \(W\) satisfying

1. exactly \(11440=B(17)-B(16)\) letters of \(W\) contain \(z\); and
2. deleting those letters leaves the byte-fixed word \(X\), in its fixed
   order and with every value unchanged.

Thus \(|W|=12873+11440=24313\). Coordinate deletion proves that this is a
natural saturated-coordinate equality face. It is not a normalization of
all possible K17 equality words: another equality word may delete to a
different K16 optimum, and no theorem here says that some coordinate must
saturate its deletion cap.

The associated rank-eight carrier is

~~~text
scratch/k16_true_fourfilter_endpoint_reroot_targets_20260731.word
SHA-256 c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906
~~~

and is used only in Section 4 to define a structured marked-envelope order.

## 2. Exact cut criterion

Number the letters of an arbitrary old-coordinate word
\(X=(x_0,\ldots,x_{n-1})\), and number its gaps \(0,\ldots,n\). Gap \(h\)
is before \(x_h\); gaps 0 and \(n\) are the two exterior gaps.

For an old target \(S\), define

\[
 e(S)=\min\{r:\bigvee_{i=l}^r x_i=S\text{ for some }l\},
 \qquad
 s(S)=\max\{l:\bigvee_{i=l}^r x_i=S\text{ for some }r\}.
 \tag{2.1}
\]

### Lemma 2.1 (occupied-cut obstruction)

If gap \(h\) contains a \(z\)-letter, the old target \(S\) can remain
covered only if

\[
                 e(S)<h\quad\text{or}\quad s(S)\ge h.       \tag{2.2}
\]

If \(h\) is the only occupied internal gap, the condition is also
sufficient. Equivalently, an insertion in \(h\) destroys \(S\), regardless
of any other insertions, whenever

\[
                    s(S)<h\le e(S).                          \tag{2.3}
\]

#### Proof

An interval with old union \(S\) cannot contain a \(z\)-letter. It must
therefore lie wholly to the left or wholly to the right of the occupied
gap. A left witness exists exactly when the earliest possible right
endpoint is below \(h\), and a right witness exists exactly when the latest
possible left endpoint is at least \(h\). This gives necessity. With no
other occupied internal gap, either witness is untouched, proving
sufficiency. Additional insertions can destroy witnesses but cannot restore
a target satisfying (2.3). \(\square\)

The smallest abstract forbidden pattern is consequently one occupied gap
and one target whose entire witness family crosses that gap. Marginal
subsequence universality misses precisely this pattern.

## 3. The fixed K16 optimum has no internal universal cut

The independent replay computes (2.1) for all \(65535\) old targets. It
finds:

~~~text
distinct (start, changed-OR) rows                 148019
targets having a nonempty forbidden gap interval  44698
maximum forbidden interval length                     7
safe gaps                                      {0,12873}
internal blocker load range                         1..14
~~~

Every one of the 12,872 internal gaps has positive blocker load. The last
internal gap is especially sharp: its sole blocker is 0xf31c. All
witnesses for 0xf31c start at or before 12868 and end at or after 12872.

### Theorem 3.1 (endpoint rigidity)

In the fixed saturated-coordinate fibre of Section 1, every \(z\)-containing
letter lies before \(x_0\) or after \(x_{n-1}\). Hence every surviving word
has the exact form

\[
                         W=P^z\,X\,Q^z,              \tag{3.1}
\]

where \(P^z\) means that \(z\) is added to every payload of \(P\),
\(|P|=t\), \(|Q|=11440-t\), and \(0\le t\le11440\).

#### Proof

If a marked letter occupied an internal gap \(h\), the audited positive
blocker load supplies a target satisfying (2.3). Lemma 2.1 says that target
is absent, contradicting universality. Multiple marked letters in an
exterior gap merely form a prefix or suffix block, giving (3.1).
\(\square\)

Thus the proposed fixed-parent interleaving or braid is closed before SAT:
retaining this particular K16 optimum literally permits only a two-ended
marked sector. This does not close rethreading or changing any old letter.

## 4. The parent rank-nine first-deadline sector

Let the authenticated carrier be \(T_0,\ldots,T_{12869}\), and put

\[
                         R_i=T_i\vee T_{i+1}.                 \tag{4.1}
\]

The audit verifies that the 12,869 values \(R_i\) all have rank nine and
contain all \(\binom{16}{9}=11440\) rank-nine masks. There are 1,429 repeat
occurrences, including 329 consecutive holds. Retaining the first
occurrence of every mask gives a canonical order

\[
                         E_0,E_1,\ldots,E_{11439}.             \tag{4.2}
\]

This is a permutation of the old rank-nine layer. Its catalogue digest is
recorded in the audit JSON.

A proof-safe structured scout may use marked payloads

\[
                   a_j\subseteq E_j,\qquad m_j=z\vee a_j,     \tag{4.3}
\]

and split the fixed order at \(t\), putting \(m_0,\ldots,m_{t-1}\) before
\(X\) and the rest after \(X\). Equation (4.3) is a restrictive envelope
choice, not a claim that the relocated \(E_j\)'s are already the maximal
envelopes of some K17 staircase. Literal final replay, rather than that
interpretation, makes the model sound.

### Coordinate-cap compression

Every coordinate of a length-24313 universal K17 word occurs in at most
11440 letters. The old-coordinate loads already present in \(X\) are

~~~text
3866 3833 3885 3891 3867 3876 3899 3912
3898 3909 3951 3960 3959 3978 3996 5260.
~~~

Hence the marked payload capacities are

~~~text
7574 7607 7555 7549 7573 7564 7541 7528
7542 7531 7489 7480 7481 7462 7444 6180.
~~~

Every coordinate occurs in exactly 6435 envelopes \(E_j\). Therefore
under (4.3) the first fifteen capacity rows are automatic. The entire
coordinate-cap hierarchy at level one reduces to the single PB row

\[
       \sum_{j:15\in E_j}[15\in a_j]\le6180.                 \tag{4.4}
\]

Equivalently at least \(6435-6180=255\) eligible marked payloads must omit
old bit 15. The base structured model has only
\(11440\cdot9=102960\) payload-bit variables, one endpoint split, envelope
zeros, and (4.4), before target blocks are activated.

## 5. Exact marked-target formula

For a payload word \(A\), let

- \(\operatorname{Cov}(A)\) be the old-coordinate ORs of its nonempty
  contiguous intervals;
- \(\operatorname{Pre}(A)\) be its nonempty prefix ORs; and
- \(\operatorname{Suf}(A)\) be its nonempty suffix ORs.

Payloads may be empty, so these families may contain the zero mask. For set
families write
\(\mathcal A\vee\mathcal B=\{a\vee b:a\in\mathcal A,b\in\mathcal B\}\).
Let \(U=\bigvee X=0xffff\). For the endpoint word \(W=P^z X Q^z\), define

\[
\begin{aligned}
 \Phi_X(P,Q)={}&\operatorname{Cov}(P)\cup\operatorname{Cov}(Q)\\
 &\cup\bigl(\operatorname{Suf}(P)\vee\operatorname{Pre}(X)\bigr)\\
 &\cup\bigl(\operatorname{Suf}(X)\vee\operatorname{Pre}(Q)\bigr)\\
 &\cup\bigl(\operatorname{Suf}(P)\vee\{U\}\vee
                    \operatorname{Pre}(Q)\bigr),             \tag{5.1}
\end{aligned}
\]

where a term involving an empty side is empty.

### Theorem 5.1 (endpoint marked-cover equivalence)

The word \(W=P^zXQ^z\) is universal on 17 coordinates if and only if

\[
                         \Phi_X(P,Q)=2^{[16]}.                \tag{5.2}
\]

#### Proof

All old targets occur in the unchanged contiguous block \(X\). Project an
interval containing \(z\) to the old coordinates. It lies wholly in \(P\),
wholly in \(Q\), crosses from a suffix of \(P\) into a prefix of \(X\),
crosses from a suffix of \(X\) into a prefix of \(Q\), or crosses both
marked sides and hence contains all of \(X\). These are exactly the five
families in (5.1), and every member of each family is realized by the
corresponding interval. Thus \(z\vee S\) occurs exactly when
\(S\in\Phi_X(P,Q)\). Include \(S=0\) for the singleton target \(z\).
\(\square\)

For this \(X\), \(\operatorname{Pre}(X)\) has only ten distinct masks and
\(\operatorname{Suf}(X)\) only nine. The two cross-boundary families are
therefore tiny compared with a raw 24,313-position interval model.

## 6. An oriented boundary-matching obstruction closes this fibre

The marked K17 targets of rank nine are exactly

\[
             z\vee S,\qquad S\in\binom{[16]}8,               \tag{6.1}
\]

so 12,870 distinct targets are required.

### Lemma 6.1 (one equal-rank delivery per oriented endpoint)

In any word, a fixed left endpoint delivers at most one distinct OR target
of a fixed rank. The same holds for a fixed right endpoint.

#### Proof

As the opposite endpoint moves, the interval ORs form an inclusion chain.
Two comparable sets of equal rank are equal. \(\square\)

For a parent word \(X\), form two boundary incidence graphs at old rank
\(r\):

- \(G^-_r(X)\) has one left vertex for every start \(a\) whose suffix OR
  \(U_a=\bigvee_{i=a}^{n-1}x_i\) has rank at most \(r\), one right vertex
  for every rank-\(r\) label \(S\), and edge \(aS\) when \(U_a\subseteq S\);
- \(G^+_r(X)\) is the reversed graph, using ends \(b\), prefix ORs
  \(V_b=\bigvee_{i=0}^{b}x_i\), and edges \(bS\) when \(V_b\subseteq S\).

Write their matching numbers as \(\mu^-_r(X)\) and \(\mu^+_r(X)\).

### Proposition 6.2 (two-oriented boundary-matching bound)

If an endpoint word \(P^zXQ^z\) has \(m=|P|+|Q|\) marked cells and covers
all marked targets of child rank \(r+1\), then

\[
                \binom dr\le
                m+\min\{\mu^-_r(X),\mu^+_r(X)\},             \tag{6.2}
\]

where \(d\) is the old dimension.

#### Proof

Map every marked rank-\((r+1)\) target to the left start of one witnessing
interval. Lemma 6.1 makes this injective. A marked start is one of the \(m\)
marked cells. An unmarked start \(x_a\) cannot reach the marked prefix; to
reach \(z\), it must extend through the entire suffix of \(X\) into \(Q\).
Its rank-\(r\) old label contains \(U_a\). The distinct targets assigned to
unmarked starts therefore form a matching in \(G^-_r(X)\), contributing at
most \(\mu^-_r(X)\). Reversing the argument and mapping targets to their
right ends gives the bound using \(\mu^+_r(X)\). Take the stronger
orientation. \(\square\)

For the authenticated \(X\), literal prefix/suffix replay gives

~~~text
eligible right ends b = 0,1,2
prefix ORs             = c3c8,c3ca,c3ca

eligible left starts a = 12869,12870,12871,12872
suffix ORs             = f30c,f30c,f30c,f30c
~~~

All four left-start vertices have the single neighbour
\(\mathtt{0xf30c}\), so \(\mu^-_8(X)=1\). On the other orientation, end 0
has the nine rank-eight supersets of \(\mathtt{0xc3c8}\), while ends 1 and
2 both have only neighbour \(\mathtt{0xc3ca}\); hence
\(\mu^+_8(X)=2\). The left-start orientation is sharpest.

### Theorem 6.3 (fixed-parent saturated-coordinate no-go)

There is no universal length-24313 K17 word whose \(z\)-deletion is the
byte-fixed K16 optimum \(X\).

#### Proof

Endpoint rigidity gives (3.1). Proposition 6.2 bounds the number of
distinct represented rank-nine marked targets by \(11440+1=11441\),
whereas (6.1) requires 12,870. The exact boundary-matching deficiency is

\[
                         12870-11441=1429>0.                 \tag{6.3}
\]

This contradiction is independent of marked payload values, their order,
the rank-nine envelope restriction, and the coordinate-cap PB row.
\(\square\)

Counting raw boundary positions without identifying their repeated labels
gives independent weaker deficiencies 1,426 from left starts and 1,427
from right ends. There is also a cross-boundary audit: a rank-eight
old projection crossing the marked-prefix/\(X\) boundary must contain the
rank-seven first cell \(\mathtt{0xc3c8}\), giving only nine possibilities;
the opposite boundary adds only \(\mathtt{0xf30c}\). Thus 12,860 projections
would have to occur internally in the two marked sectors, which have only
11,440 right endpoints. This gives deficiency 1,420 and agrees with the
stronger oriented count.

This theorem closes the proposed literal K16-subsequence scout before any
H100 solve. To remain viable, an equality construction must change or
rethread the z-free optimum, delete to a different optimum with a nontrivial
universal cut structure, or avoid saturating one coordinate.

## 7. Proof-safe PB/CNF CEGAR semantics

Fix one split \(t\); the 11,441 split faces can be scanned independently.
Use Boolean variables \(a_{j,b}\) only for \(b\in E_j\), impose (4.4), and
activate exact witness blocks lazily.

For an active marked target \(z\vee S\), a standard three-phase
before/inside/after boundary word selects a nonempty interval in one of the
five classes of (5.1). Conditional clauses enforce:

1. no selected fixed parent letter or marked payload contains a bit outside
   \(S\);
2. for every \(b\in S\), a selected fixed parent letter supplies \(b\), or
   some selected marked position has \(a_{j,b}=1\); and
3. the selected interval meets a marked position.

Tseitin variables for inside-AND-\(a_{j,b}\) make these ordinary CNF
clauses. Conversely any literal witness interval satisfies the block, so it
is equisatisfiable, not merely necessary. Formula (5.1) permits the parent
portion to be compressed to its ten prefix and nine suffix OR states.

The exact CEGAR loop is:

1. solve the current payload/envelope/cap model;
2. materialize \(P^zXQ^z\);
3. replay all \(65536\) marked targets literally;
4. if holes remain, add their exact witness blocks and repeat;
5. accept SAT only after a full 131,071-target replay.

Old targets need no CEGAR blocks because Theorem 3.1 leaves \(X\) contiguous.
UNSAT at any round is a valid no-go for that fixed split and envelope order;
SAT before the final replay is not a construction. For the present fixed
parent, Theorem 6.3 makes such a run theorem-redundant; the formulation is
retained as an exact template for other deletion parents.

## 8. Independent finite validation

The retained audit

~~~text
scratch/audit_k17_saturated_coordinate_endpoint_split_cegar_20260731.py
scratch/k17_saturated_coordinate_endpoint_split_cegar_20260731.audit.json
~~~

performs the following independently of any SAT generator:

- authenticates both K16 inputs;
- replays all 65,535 old targets and the full cut criterion;
- verifies that the only safe gaps are the two exterior gaps;
- authenticates the 11,440-mask first-deadline order;
- derives the single nontrivial coordinate PB row (4.4);
- verifies boundary matching numbers \((\mu^-_8,\mu^+_8)=(1,2)\) and the
  exact deficiency 1,429, plus the weaker raw-start/raw-end/cross-boundary
  deficiencies 1,426, 1,427, and 1,420;
- exhausts all 48 endpoint payload/split cases over the K2 optimum and all
  2,048 cases over a K3 optimum, comparing (5.1) to direct marked-interval
  replay in every case; and
- replays the saturated equality examples

~~~text
K2 -> K3:  6 4 | 1 2
K2 -> K3:  4 | 1 2 | 4
K3 -> K4:  10 12 8 | 1 2 4 1
~~~

as well as the minimal internal-insertion failure 1 4 2, which loses the
old target 3.

The JSON is byte-identical on a fresh replay. No split face should be
launched: all 11,441 are closed simultaneously by Theorem 6.3. The result
does not rule out changing or rethreading the z-free K16 parent and makes no
unrestricted K17 claim.
