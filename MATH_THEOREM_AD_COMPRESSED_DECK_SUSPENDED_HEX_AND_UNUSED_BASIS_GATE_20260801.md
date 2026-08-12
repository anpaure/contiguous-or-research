# A compressed-deck suspended-hex family is exact but boundary-injective

Date: 2026-08-01  
Lane: AD, buffered ECO / unused compiler basis  
Status: exact local construction, exact obstruction boundary, and conditional selection interface.  No additive-constant or all-`m` construction is claimed.

## 0. Result

The compressed prefix/suffix/internal OR-deck criterion is genuinely useful,
but it does not make an arbitrary retained ECO path eligible.  Two exact
facts delimit the current packet problem.

1. There is an owner-preserving eight-letter suspended-hex rethread whose
   old and new words have **equal** prefix, suffix, and internal interval OR
   deck supports.  Across all labelled terminal boundaries, a fixed active
   hex has

   \[
             2|K|\bigl(|\Omega|-|K|-4\bigr)                 \tag{0.1}
   \]

   labelled padded realizations.  In the specialization
   `|Omega|=2n, |K|=n-1`, this is exactly
   `2(n-1)(n-3)=Theta(n^2)` for `n>=4`.

2. This is **not** a quadratic menu at one fixed word slot.  The terminal
   owner uniquely determines `(p,r,t)`, so a fixed ordered boundary has at
   most one option from this family.

3. This raw macro is not itself a carrier packet: one lower seam colour and
   two upper seam colours repeat, and both phases have an internal positive
   run of length one.  It also has no certified deletion cell in a fixed
   unused compiler basis.  Thus its fully guarded/resident catalogue is
   empty before further structured thickening.

The independently authenticated fourteen-owner retained detour is a
strictly stronger negative calibration: among its `28^2=784` old/new
cut-orientation pairs, neither directed replacement satisfies compressed
prefix/suffix/internal OR-deck dominance.  Hence the live theorem is not
"pad any ECO path".  It is to construct a **structured owner-preserving
resident profile** whose free parameters do not all leak into its connector
boundary, and which supplies a literal unused-basis deletion label.

## 1. Compressed decks and owner rigidity

For a word `W=(W_1,...,W_h)`, write

\[
\begin{aligned}
 \mathcal P(W)&=\{W_1\cup\cdots\cup W_j:1\le j\le h\},\\
 \mathcal S(W)&=\{W_j\cup\cdots\cup W_h:1\le j\le h\},\\
 \mathcal I(W)&=\{W_i\cup\cdots\cup W_j:1\le i\le j\le h\}.
                                                               \tag{1.1}
\end{aligned}
\]

The replacement theorem in
`MATH_THEOREM_COMPRESSED_PREFIX_SUFFIX_DECK_TRANSPARENCY_20260801.md`
says that

\[
 \mathcal P(X)\subseteq\mathcal P(Y),\quad
 \mathcal S(X)\subseteq\mathcal S(Y),\quad
 \mathcal I(X)\subseteq\mathcal I(Y),\quad
 \bigcup X=\bigcup Y                                      \tag{1.2}
\]

preserves every old interval union in every exterior context.

Internal dominance has an important rigidity which is absent from the
prefix and suffix rows.

### Lemma 1.1 (uniform-rank singleton rigidity)

Let every letter of `X` and `Y` have rank `m`.  If
`mathcal I(X) subseteq mathcal I(Y)`, then every distinct letter occurring
in `X` also occurs as a letter of `Y`.  In particular, if `X` has `h`
distinct letters and `Y` has length `h`, then the letters of `Y` are exactly
those of `X`, in some order.

#### Proof

For a letter `A` of `X`, the singleton interval gives
`A in mathcal I(X)`.  Hence some nonempty interval of `Y` has union `A`.
Every rank-`m` letter in that interval is a subset of the rank-`m` set `A`,
so it equals `A`.  Thus `A` occurs in `Y`.  The equal-length conclusion
follows by counting.  \(\square\)

Consequently a fixed-length middle-owner packet cannot obtain internal OR
dominance by silently replacing one old owner with a fresh owner.  Fresh
rail letters must occur in both phases or be paid for by a longer word.

## 2. Exact eight-owner macro

Let `Omega` be a finite ground set.  Fix

\[
 K\subseteq\Omega,\qquad
 a,b,c,s\in\Omega-K\text{ distinct},                         \tag{2.1}
\]

choose `r in K`, and choose

\[
              t\in\Omega-\bigl(K\cup\{a,b,c,s\}\bigr).       \tag{2.2}
\]

Put `K_0=K-{r}` and

\[
                         X_{uv}=K\cup\{u,v\}.                  \tag{2.3}
\]

The two suspended-hex paths are

\[
\begin{aligned}
 O_6&=(X_{ab},X_{bs},X_{as},X_{ac},X_{bc},X_{cs}),\\
 N_6&=(X_{ab},X_{as},X_{bs},X_{bc},X_{ac},X_{cs}).             \tag{2.4}
\end{aligned}
\]

For a polarity `p in {a,b}`, append the common two-letter rail

\[
 R_0^{p}=K_0\cup\{p,c,s\},\qquad
 R_1^{p}=K_0\cup\{p,c,t\},                                   \tag{2.5}
\]

and set

\[
                         O^p=O_6R_0^pR_1^p,qquad
                         N^p=N_6R_0^pR_1^p.                    \tag{2.6}
\]

### Theorem 2.1 (compressed-deck family and boundary injection)

For each polarity `p`:

1. `O^p` and `N^p` are literal eight-letter Johnson paths on rank
   `|K|+2` owners;
2. they have the same first and last owners and exactly the same eight
   owner letters;
3. their total unions agree; and
4. their three compressed OR deck support sets agree exactly:

\[
 \mathcal P(O^p)=\mathcal P(N^p),\qquad
 \mathcal S(O^p)=\mathcal S(N^p),\qquad
 \mathcal I(O^p)=\mathcal I(N^p).                              \tag{2.7}
\]

For fixed `(K,a,b,c,s)`, the labelled choices `(p,r,t)` give exactly
(0.1) distinct candidatewise exchanges.  Their terminal owners are all
distinct.  Hence fixing the ordered endpoint pair leaves at most one
exchange in this family.

#### Proof

Every consecutive pair in (2.4) exchanges one active coordinate.  The edge
`X_cs R_0^p` deletes `r` and adds `p`, and `R_0^p R_1^p` deletes `s` and
adds `t`.  Thus both words are Johnson paths.  Equation (2.4) is a
permutation of the same six owners, and the last two owners are common.

Suppress the common set `K_0` and write a union by concatenating its active
coordinate names.  For polarity `a`, the common decks are

\[
\begin{aligned}
 \mathcal P={}&\{rab,rabs,rabcs,rabcst\},\\
 \mathcal S={}&\{act,acst,racst,rabcst\},                     \tag{2.8}\\
 \mathcal I={}&\{acs,acst,act,rab,rabc,rabcs,rabcst,rabs,\\
               &\qquad rac,racs,racst,ras,rbc,rbcs,rbs,rcs\}.
                                                                    \tag{2.9}
\end{aligned}
\]

Direct accumulation along either word gives (2.8)--(2.9).  The polarity
`b` case is obtained by the corresponding `a/b` interchange in the final
rail; the audit enumerates it separately.  This proves (2.7) and total-union
equality.

There are two choices of polarity, `|K|` choices of `r`, and
`|Omega|-|K|-4` choices of `t`.  The terminal owner

\[
                     R_1^p=(K-\{r\})\cup\{p,c,t\}              \tag{2.10}
\]

recovers `p` as its member in `{a,b}`, recovers `r` as the unique missing
member of `K`, and then recovers `t`.  Thus different triples have distinct
terminal endpoints, proving both the count and fixed-boundary assertion.
\(\square\)

By (1.2), either phase may replace the other without losing any old upper
interval value in any exterior context.  This is a genuine positive result
which pointwise first/last occurrence timing would miss.

Here and throughout (2.7)--(2.9), a deck is the set of distinct values in
(1.1).  No equality of ordered suffix sequences, interval-length grading,
or deck multiplicities is asserted.

## 3. Exact failed rows

The macro in Theorem 2.1 is not yet an admissible rainbow/resident packet.
Its lower seam-colour sequence in the two phases is

\[
\begin{aligned}
 O^p:&\quad Kb,Ks,Ka,Kc,Kc,K_0cs,K_0pc,\\
 N^p:&\quad Ka,Ks,Kb,Kc,Kc,K_0cs,K_0pc.                        \tag{3.1}
\end{aligned}
\]

Thus `Kc` occurs twice.  The upper seam multisets also agree, but the six
active seams contain `K union {a,b,s}` twice, and the padded word has only
five distinct upper seam colours among seven seams.  Hence this literal
path cannot simply replace a q1-rainbow path.

It also fails residence without exterior ambiguity.  For both polarities,
the new word has an internal one-letter `a`-run and the old word has an
internal one-letter `b`-run.  Therefore any
minimum positive-run threshold at least two rejects the corresponding
on/off pair before boundary runs are considered.  The fresh coordinate `t`
also has a one-letter terminal run, though that one could in principle be
extended by the right exterior.

Finally, `(p,r,t)` is not by itself a compiler deletion cell.  No claim is
made that any of the raw macros preserves a trace-guarded compiler matching
or deletes a cell in its unused dual basis.

### Proposition 3.1 (current effective abundance)

For the exact unbuffered family (2.6):

* compressed-deck eligible candidatewise exchanges across all boundaries:
  exactly the raw count (0.1);
* compressed-deck choices at one fixed ordered boundary: at most one;
* q1-rainbow choices: zero;
* choices residence-safe in both phases at threshold at least two: zero;
* fully transparent unused-basis choices currently certified: zero.

Thus (0.1) is a real global geometry/deck count, not a protected list-size
theorem.  The fixed-boundary fibre fails the quadratic-menu requirement even
before the palette, residence, and compiler rows are imposed.

## 4. The calibrated retained-detour obstruction

The explicit fourteen-owner common retained detour in
`scratch/audit_independent_eco_signature_marker_detour_20260731.py` has
`28` linearizations in each phase.  The current audit tests all `784` pairs
and reports

```text
pointwise_hits       0
compressed_forward  0
compressed_reverse  0
```

where each compressed direction checks all four rows in (1.2).  Its
canonical audit payload is

```text
717b3c39b979d247126a495f9090eb907ea4b90da7b8544cd5d14f8ac815e7df
```

This no-go and Theorem 2.1 do not conflict.  The negative face is a fixed
fourteen-owner retained detour inside the contracted all-six ECO connector;
Theorem 2.1 uses a different owner-preserving six-owner permutation and a
special correlated two-letter rail whose free parameters alter its terminal
endpoint.  The no-go proves that arbitrary common
retained paths cannot be promoted by merely weakening pointwise timing to
compressed decks.

## 5. Exact unused-basis and selection interface

Fix a trace-guarded compiler matching `M_0` and let

\[
                    B=C-\operatorname{cells}(M_0)               \tag{5.1}
\]

be its unused-cell bank.  Suppose a structured thickening of (2.6) assigns
to every surviving option `q` a literal deletion cell `beta(q)` and obeys:

1. the four compressed-deck rows (1.2);
2. the required residence boundary state and internal run condition;
3. a common physical connector/topology boundary;
4. no deletion or guard change on an incidence used by `M_0`; and
5. `beta(q) in B`.

Then any mutually compatible family with distinct `beta(q)` values composes
while preserving all old upper coverage and the same matching `M_0`.  This
is exactly the transparent-unused-basis composition theorem with its upper
row weakened from pointwise signatures to compressed decks.

For quantitative selection, require a complete conflict tokenization: every
incompatible pair shares at least one exported token.  Let every option
export at most `s` physical, residence, topology, and compiler tokens.  If
each such token occurs in at most `lambda` options over all other task lists
combined, then the option conflict graph has

\[
                              \Delta\le s\lambda.                \tag{5.2}
\]

In particular every list's average external row energy is at most
`s lambda` under this aggregate-load convention.  If the load bound is only
per other list, the corresponding bound is `(H-1)s lambda` for `H` task
lists.

Consequently Haxell's independent-transversal theorem applies whenever
every post-pruning list has at least `max(1,2s lambda)` options.  If a
structured resident thickening has `s=O(d)`, `lambda=O(n)` and retains
`Theta(n^2)` options, this row is asymptotically sufficient for `d=o(n)`.

This is conditional on the actual thickening and token-load code.  The raw
eight-owner family has at most one option at a fixed boundary and zero
residence-safe options, while the calibrated
fourteen-owner face has zero compressed-deck options, so neither currently
instantiates (5.2).

## 6. Sharp remaining construction gate

The next theorem must provide, simultaneously:

1. an owner-preserving structured profile, as forced by Lemma 1.1, with a
   quadratic fibre over one fixed connector boundary (or an equally strong
   joint anchor-boundary assignment theorem);
2. q1 palette compensation without destroying (1.2);
3. residence-safe correlated rails in both phases;
4. one common connector boundary; and
5. a literal task-to-unused-cell map `beta` preserving one trace-guarded
   compiler matching.

Rail padding which only equalizes plateau timing is insufficient.  The
fourteen-owner `0/784` certificate shows that even the compressed deck can
fail everywhere, while Proposition 3.1 shows that deck transparency alone
can coexist with zero guarded options.

## 7. Reproducible audit

Run

```bash
python3 scratch/audit_ad_compressed_deck_suspended_hex_macro_20260801.py
python3 scratch/audit_independent_eco_signature_marker_detour_20260731.py
```

The first script verifies both polarities, literal Johnson legality,
candidatewise common endpoints and owner set, the exact `4/4/16`
prefix/suffix/internal deck
sizes, identical lower/upper seam multisets, their repetitions, internal
one-runs, and the count formula.  It writes

```text
scratch/audit_ad_compressed_deck_suspended_hex_macro_20260801.audit.json
```

with canonical payload SHA-256

```text
3ebe7e96e1474c9795ad006c482d0d100013c70e7b8b989a8339bd8fe32af351
```

The second script independently freezes the `0/784` retained-detour
calibration quoted in Section 4.
