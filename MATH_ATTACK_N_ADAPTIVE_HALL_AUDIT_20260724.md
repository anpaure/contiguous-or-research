# Cross-audit of `MATH_ATTACK_N_ADAPTIVE_HALL_REPORT_RAW_20260724.md`

Date: 2026-07-24  
Method: theorem-level audit only; no web search and no finite/computational search.

## 0. Verdict key and overall conclusion

- **VALID** means that the displayed assertion follows with the stated or standard conventions.
- **CORRECTED** means that the underlying assertion is usable only after the scope, indexing, hypothesis, or conclusion stated below is substituted.
- **UNSUPPORTED** means that the report does not supply, and the present audit does not find, a proof of the assertion. It does not necessarily mean the assertion is false.

The report's main outcome is **VALID**:

\[
\mathrm{SDH}_A/\mathrm{AO}_A
\quad\text{is neither proved nor disproved by the report.}
\]

The exact adaptive-state equations, the one-coordinate Hall calculation, the canonical configuration determinant, the abstract cube obstruction, and the abstract one-rewire cascade all survive audit, subject to the corrections below. The important overstatements are:

1. a toggle *stage* run and its rotated deletion-word block differ by one endpoint in their indexing;
2. balanced union histograms require a previously balanced/admissible history;
3. the determinant-\(2\) minor refutes total unimodularity only for the exhibited natural configuration matrix, not every flow, extended, or matroidal formulation;
4. the claimed second determinant-\(2\) minor in a time-expanded matrix is not exhibited and is unsupported;
5. the cube and rewire examples live in abstract Johnson-supported selector graphs, not in a single completed exact factor;
6. the symbol \(\nu_q^{\rm can}\) and hence the general displayed resource inequality are undefined in the report;
7. arbitrary reachable carries preserve the shallow per-wreath **matching**, but not the canonical Hamilton difference-label identity or the cyclic-union identity;
8. the fixed-window equivalence is only the fixed-\(A\), same-method equivalence between the weighted and unweighted toggle objectives. It is not an equivalence with the labelled common-owner theorem, with unrestricted growing windows, or with the unlabelled MWB/GW statement.

## 1. Conventions used in the audit

Let

\[
n=2m+1,\qquad W=\binom{n}{m},\qquad
N_q=\binom{n}{m-q},\qquad B=\frac Wn,
\]

and write

\[
W=c_qN_q+\rho_q,\qquad 0\le \rho_q<N_q.
\]

All graph edge counts below count labelled owner edges with multiplicity. Orienting an owner edge toward an endpoint means assigning that owner to that endpoint; endpoint load is indegree. Unless explicitly prescribed, the set of the \(\rho_q\) vertices of load \(c_q+1\) is free.

Assume throughout that the audited window satisfies \(K+1\le m\). For a fixed owner \(X\), its canonical deletion word is
\(a_1,\ldots,a_{K+1}\),

\[
L_q=X\setminus\{a_1,\ldots,a_q\},
\]

and \(\varepsilon_q=1\) denotes a stage-\(q\) toggle. The audit concerns exactly this one ascending pass through the stages.

## 2. Adaptive-state and interval-composition identities

### 2.1 Carried-letter recurrence

**Verdict: VALID.** Define

\[
\kappa_1=a_1,
\qquad
\kappa_{q+1}=
\begin{cases}
\kappa_q,&\varepsilon_q=1,\\
a_{q+1},&\varepsilon_q=0.
\end{cases}
\]

Then induction on \(q\) gives

\[
P_q=L_{q+1}\cup\{\kappa_{q+1}\}.
\]

Immediately before the stage-\(q\) choice, the two legal endpoints are

\[
u=L_q=L_{q+1}\cup\{a_{q+1}\},
\qquad
v=L_{q+1}\cup\{\kappa_q\}.
\]

The deletion letters are distinct, and
\(\kappa_q\in\{a_1,\ldots,a_q\}\), so
\(\kappa_q\ne a_{q+1}\). Hence

\[
u\cap v=L_{q+1},
\qquad
u\cup v=L_q\cup\{\kappa_q\}=P_{q-1}.
\]

After the decision,
\(P_q=L_q\) exactly when \(\varepsilon_q=0\). Therefore the one-pass mismatch count is exactly

\[
e_q=\#\{X:P_q(X)\ne L_q(X)\}=T_q.
\]

No signed relaxation is used in these identities.

### 2.2 Toggle runs versus rotated blocks

**Verdict: CORRECTED (off-by-one ambiguity).** A block of deletion-word **positions**
\([s,t]\) is rotated by toggling the **stages**

\[
s,s+1,\ldots,t-1.
\]

Equivalently,

\[
(a_s,a_{s+1},\ldots,a_t)
\longmapsto
(a_{s+1},\ldots,a_t,a_s),
\]

and for \(s\le q<t\),

\[
P_q=L_{q+1}\cup\{a_s\}.
\]

If the phrase “toggle run \([s,t]\)” is intended to mean
\(\varepsilon_s=\cdots=\varepsilon_t=1\), then the rotated position block is instead \([s,t+1]\). For example, toggling stages \(1,2\) rotates
\((a_1,a_2,a_3)\), not merely \((a_1,a_2)\).

With that indexing repaired, maximal toggle-stage runs give a disjoint interval composition of the deletion word, and conversely such an interval composition determines all one-pass decisions. Thus the static interval-composition formulation is **VALID for this one ascending pass**. It does not parametrize arbitrary nested resolutions or arbitrary multi-pass dynamics.

### 2.3 Fixed-window weighted/unweighted equivalence

**Verdict: VALID WITH SCOPE CORRECTION.** The exact ratio is

\[
\lambda_q:=\frac{W}{N_q}
=\prod_{i=0}^{q-1}\frac{m+2+i}{m-i}.
\]

Since

\[
\log\lambda_q
\le \sum_{i=0}^{q-1}\frac{2(i+1)}{m-i}
\le \frac{q(q+1)}{m-q+1},
\]

for each fixed \(A\), all sufficiently large \(m\), and
\(q\le K_A:=\lceil A\sqrt m\rceil\), one has

\[
1\le c_q=\lfloor\lambda_q\rfloor
\le C_A:=\left\lceil e^{A^2+2}\right\rceil.
\]

The harmless \(+2\) absorbs the ceiling in \(K_A\) and the finite large-\(m\) threshold. Consequently, for the same exact factor and the same one-pass decisions,

\[
C_A^{-1}\sum_{q\le K_A}T_q
\le
\sum_{q\le K_A}\frac{T_q}{c_q}
\le
\sum_{q\le K_A}T_q.
\]

Therefore an \(o(W)\) bound for either sum is equivalent to an \(o(W)\) bound for the other, for each fixed \(A\). This is the precise \(\mathrm{SDH}_A\leftrightarrow\mathrm{AO}_A\) equivalence asserted by the report.

The following stronger readings are **UNSUPPORTED/INCORRECT**:

- uniform equivalence when \(A=A(m)\) grows;
- equivalence with labelled common-owner synchronization;
- equivalence with the unlabelled MWB/GW theorem without the separate fixed-\(A\) diagonalization argument;
- equivalence between this one-pass static composition problem and every possible adaptive resolution.

## 3. Graph rewiring and evolving histograms

### 3.1 Exact rewiring identity

**Verdict: VALID.** For \(q\ge2\),

\[
\kappa_q=a_q\iff\varepsilon_{q-1}=0.
\]

Thus \(G_q\) is obtained from the canonical graph \(H_q\) by changing exactly the alternate endpoint of each labelled owner edge toggled at stage \(q-1\). The anchor \(L_q\) and intersection \(L_{q+1}\) remain fixed. There are exactly \(T_{q-1}\) such labelled edges, even if parallel unlabelled edges occur.

For every vertex family \(U\), with \(e_G(U)\) denoting the number of edges internal to \(U\), counted with multiplicity,

\[
\bigl|e_{G_q}(U)-e_{H_q}(U)\bigr|\le T_{q-1}.
\]

Each rewired labelled edge changes the internal-edge indicator by at most one, which proves the bound. At \(q=1\), \(G_1=H_1\).

### 3.2 Histograms

**Verdict: VALID, EXCEPT FOR ONE MISSING CONDITION.** Exactly:

\[
\text{intersection histogram}=\mu_{q+1},
\qquad
\text{anchor histogram}=\mu_q,
\qquad
\text{union histogram}=b_{q-1}.
\]

The last identity follows from
\(u_X\cup v_X=P_{q-1}(X)\). The statement

\[
b_{q-1}(T)\in\{c_{q-1},c_{q-1}+1\}
\]

is **CORRECTED** to: it holds when the preceding state is assumed balanced, as it is along an admissible \(\mathrm{AO}_A\) history. It is not an unconditional invariant of an arbitrary toggle history.

The report's warning that support can be sparse while the effect retains long memory is **VALID**: on a long toggle run, \(\kappa_q\) can be an arbitrarily old deletion letter even though only the immediately preceding toggle set determines which labelled edges differ from \(H_q\).

## 4. Hall cuts, point margins, and static defect

### 4.1 Point-margin recurrence

**Verdict: VALID.** Put \(r=m-q\) and define, with the baseline appropriate to each depth,

\[
\Delta_{q,x}=\#\{X:x\in P_q(X)\}-rB.
\]

Exact-factor homogeneity gives

\[
\#\{X:x\in L_s(X)\}=(m-s)B
\]

and each deletion position contains each coordinate exactly \(B\) times. Hence, for
\(C_q(x)=\#\{X:\kappa_q(X)=x\}\),

\[
C_q(x)=B+\Delta_{q-1,x}.
\]

Changing the stage-\(q\) choice from canonical to toggled replaces
\(a_{q+1}\) by \(\kappa_q\) in the selected endpoint, so

\[
\Delta_q
=\sum_{X:\varepsilon_q(X)=1}
\left(\mathbf e_{\kappa_q(X)}-\mathbf e_{a_{q+1}(X)}\right).
\]

It follows exactly that

\[
\|\Delta_q\|_1\le2T_q,
\qquad
\|\Delta_q\|_\infty\le T_q.
\]

### 4.2 Exact point-star counts

**Verdict: VALID.** For
\(U_x=\{S:x\in S\}\subseteq\binom{[n]}r\), no edge is a loop because
\(\kappa_q\ne a_{q+1}\). Direct counting gives

\[
e_{G_q}(U_x)=(r-1)B,
\]

\[
|\partial_{G_q}(U_x)|=B+C_q(x),
\]

\[
e_{G_q}(U_x^c)=(n-r)B-C_q(x).
\]

Here parallel owner edges are counted separately.

### 4.3 Hall/orientation criterion and all four slacks

**Verdict: VALID FOR AN UNPRESCRIBED HIGH-LOAD SET.** A multigraph with \(W=cN+\rho\) edges has an orientation with every indegree in \(\{c,c+1\}\) if and only if, for every vertex set \(U\),

\[
e(U)\le(c+1)|U|,
\qquad
e(U)\le c|U|+\rho.
\]

The first inequality is the upper-capacity cut. The lower-capacity cut
\(e(U)+|\partial U|\ge c|U|\) becomes the second inequality after taking complements. This criterion lets the \(\rho\) high-load vertices be chosen by the orientation; separately prescribing them would require stronger cuts.

Let

\[
\gamma=(c_q+1)N_q-W=N_q-\rho_q>0.
\]

Using \(|U_x|=rN_q/n\), the four slacks are exactly

\[
(c_q+1)|U_x|-e(U_x)
=\frac{(c_q+1)N_q+(r-1)\gamma}{n},
\]

\[
c_q|U_x|+\rho_q-e(U_x)
=\frac{c_qN_q+(n-r+1)\rho_q}{n},
\]

\[
(c_q+1)|U_x^c|-e(U_x^c)
=\frac{(n-r)\gamma}{n}+C_q(x),
\]

\[
c_q|U_x^c|+\rho_q-e(U_x^c)
=\frac{r\rho_q}{n}+C_q(x).
\]

Every term is nonnegative for every legal history. Therefore the conclusion

\[
\text{no point star or point-star complement witnesses failure of
unprescribed balanced orientation}
\]

is **VALID**. “Any obstruction is higher-order” must be read in exactly that sense; it does not address a separately prescribed high-quota vector or a simultaneous multi-depth owner constraint.

### 4.4 Static Hall defect

**Verdict: VALID AS A NECESSARY CONDITION ONLY.** If

\[
\mathfrak d_q(F)=
\max_U\left\{
\bigl(e_{H_q}(U)-(c_q+1)|U|\bigr)_+,
\bigl(e_{H_q}(U)-c_q|U|-\rho_q\bigr)_+
\right\},
\]

then a feasible \(G_q\), together with the rewiring bound, yields

\[
\mathfrak d_q(F)\le T_{q-1}.
\]

With \(T_0=0\),

\[
\mathfrak d_1(F)=0,
\qquad
\sum_{q\le K_A}\mathfrak d_q(F)
\le\sum_{q<K_A}T_q.
\]

Thus an \(o(W)\)-toggle solution has \(o(W)\) total canonical Hall defect. The converse is **UNSUPPORTED**: the inequalities neither coordinate one factor across depths nor bound supported recourse distance.

## 5. Configuration integrality

### 5.1 Exhibited determinant-\(2\) minor

**Verdict: VALID AFTER ADDING A DISJOINTNESS HYPOTHESIS.** Require

\[
R\cap\{a,b,c,d\}=\varnothing,
\qquad |R|=m-3,
\]

with \(a,b,c,d\) distinct. For

\[
X=R\cup\{a,b,c\},\quad(a_1,a_2,a_3)=(a,b,c),
\]

\[
Y=R\cup\{d,b,c\},\quad(a_1,a_2,a_3)=(d,b,c),
\]

put

\[
A=R\cup\{b,c\},\qquad C=R\cup\{c\}.
\]

The relevant configuration targets are

\[
X:(0,1)\mapsto(A,R\cup\{b\}),
\]

\[
X:(1,0)\mapsto(R\cup\{a,c\},C),
\]

\[
Y:(0,0)\mapsto(A,C).
\]

On the rows “owner \(X\), depth-\(1\) target \(A\), depth-\(2\) target \(C\),” these columns give

\[
\begin{pmatrix}
1&1&0\\
1&0&1\\
0&1&1
\end{pmatrix},
\qquad \det=-2.
\]

Therefore this natural local legal-word configuration matrix is not totally unimodular.

### 5.2 What the minor does not prove

The following stronger claims are **UNSUPPORTED**:

- that the displayed local words co-occur in one exact factor;
- that the actual right-hand side of the desired capacity system has a fractional vertex or an integrality gap;
- that no alternative totally unimodular extended formulation exists;
- that no single-commodity-flow formulation of a different architecture can exist;
- that no two-matroid-intersection reformulation can exist.

At most, the minor rules out a direct TU proof for the exhibited natural matrix. Also, “an intersection of at least three partition systems” accurately describes the owner and per-depth *upper-capacity* constraints, but lower quotas/equalities are covering constraints and are not literally just an intersection of partition matroids.

The report's sentence that “the direct time-expanded owner-flow matrix also contains an independently audited determinant-\(2\) minor” is **UNSUPPORTED**: no such matrix, row/column selection, or determinant calculation is supplied in the report. It must be deleted or accompanied by the actual minor.

## 6. Point-balanced hypercube obstruction

### 6.1 Hamilton cycle with balanced quarter defect

**Verdict: VALID, WITH THE CHECKPOINTS CLARIFIED.** For \(d=2\), use \(Q_2\). For \(d\ge4\), write
\(Q_d=Q_2\times Q_{d-2}\), let

\[
t_0=00,quad t_1=10,quad t_2=11,quad t_3=01,
\]

and, in the lower fibre \(Q_{d-2}\), let

\[
y_0=0,quad y_1=e_1,quad y_2=e_1+e_2,quad y_3=e_2.
\]

For each \(i\), choose a Hamilton path in the fibre from \(y_i\) to
\(y_{i+1}\) (indices modulo four) by deleting the edge
\(y_iy_{i+1}\) from a Hamilton cycle containing it. Traverse this path in fibre \(t_i\), then cross to fibre \(t_{i+1}\) at \(y_{i+1}\). The four paths and four cross edges form a Hamilton cycle of \(Q_d\).

The report's displayed checkpoints
\(0,e_1,e_1+e_2,e_2\) must therefore be read as the **lower-fibre** checkpoints. The full quarter vertices are

\[
A=(t_0,y_0),\quad B=(t_1,y_1),\quad
C=(t_2,y_2),\quad D=(t_3,y_3).
\]

They satisfy, coordinatewise,

\[
\mathbf1_A+\mathbf1_C=\mathbf1_B+\mathbf1_D.
\]

Start with a directed Hamilton cycle and reverse the quarter arcs
\(A\to B\) and \(C\to D\). Endpoint loads become \(2\) at
\(A,C\), \(0\) at \(B,D\), and \(1\) elsewhere. A cycle has only two orientations with indegree one at every vertex. The constructed orientation differs from each on exactly two quarter arcs, hence on

\[
2\cdot 2^{d-2}=2^{d-1}
\]

edges. Its signed point defect is zero by the displayed indicator identity.

### 6.2 Johnson embedding and uniqueness of owners/cores

**Verdict: VALID.** Choose \(d\) disjoint coordinate pairs
\(\{u_i^0,u_i^1\}\) and a disjoint base \(C_0\) of size \(r-d\), and set

\[
\phi(x)=C_0\cup\{u_i^{x_i}:1\le i\le d\}.
\]

This requires

\[
d\le\min(r,n-r).
\]

At \(q=1\), \(r=m-1\), so \(d\le m-1\). A cube edge flipping coordinate \(i\) has a union containing both members of pair \(i\) and an intersection containing neither; every other pair contributes exactly one member. Hence the flipped pair and all fixed bits are recoverable from either the union or the intersection. Distinct cube edges therefore have distinct unions and distinct intersections.

### 6.3 Isolation in the bare selector

**Verdict: VALID ONLY IN THE BARE ONE-EDGE-PER-OWNER SELECTOR.** Facets of a fixed \(m\)-owner form a clique in the Johnson graph, whereas an induced cube is triangle-free, so an owner has at most two cube facets. For \(d\ge4\), the embedding has \(m\ge5\), leaving at least two noncube facets for every nonforced owner. For \(d=2\), a noncycle owner has at most one cube facet—two would determine one of the already forced cube edges—again leaving two outside facets when \(m\ge3\). Thus all other owners can select edges avoiding the cube.

This proves isolation for an arbitrary \(q=1\) owner selector. It does **not** prove that those choices arise from a common exact wreath factor, respect the cyclic packet constraints, or admit an exact-factor completion.

### 6.4 Overload and point-margin scope

**Verdict: CORRECTED.** For \(q=1\) and \(m>2\), \(c_1=1\). If the cube were an isolated component of an actual graph, it has as many edges as vertices; therefore any globally legal lower load on the component forces load exactly one at every cube vertex. The displayed orientation has component floor-overload

\[
(2-1)+(2-1)=2
\]

and requires \(2^{d-1}\) toggles to repair.

The phrase “its overload would be only \(2\)” is valid for the isolated block's contribution. It is not a statement that an arbitrary completed exact factor has total overload \(2\); that would require a balanced complement.

The signed point defect and the associated first-order deletion-label margins vanish. Thus the example genuinely shows that first-order point balance cannot bound supported transport in the broad Johnson selector class.

The displayed general resource inequality

\[
(q+1)\mu_q(S)+q\nu_q^{\rm can}(S)
\le\binom{m+q+1}{q}
\]

is **UNSUPPORTED AS WRITTEN**, because \(\nu_q^{\rm can}\) is not defined in the report and no derivation is given. Under the natural \(q=1\) interpretation for the 2-regular cube, the claimed local cap is harmless (one obtains a left side at most \(4\le m+2\)), but that does not prove the displayed general formula.

### 6.5 Exact logical force of the cube

**Verdict: VALID AFTER RESTRICTION.** The cube refutes a black-box theorem of the form

\[
\text{Hall-feasible Johnson-supported graph}
+\text{ first-order point balance}
\Longrightarrow
\text{short supported repair}
\]

for arbitrary selector components satisfying the listed local properties. It does not refute such a theorem after adding exact cyclic packetization, common-factor completion, or protected isolation. In particular it is not an exact-factor obstruction.

## 7. One-rewire recourse cascade

### 7.1 Abstract graph calculation

**Verdict: VALID.** Let \(M=2^d\). Delete an edge \(hk\) from a Hamilton cycle of a \(Q_d\), obtaining a path of \(M-1\) edges from \(k\) to \(h\). Add a new vertex \(s\), an edge \(sk\), and a special edge \(sh\). Select the endpoint nearer \(s\) on the \(s\)-to-\(h\) path and select \(s\) on \(sh\). The loads are \(2\) at \(s\), \(0\) at \(h\), and \(1\) elsewhere. Flipping only \(sh\) repairs the canonical component.

Now rewire the special edge from \(sh\) to a second parallel \(sk\), while retaining its selected anchor \(s\). In every all-one orientation, the leaf \(h\) forces the last path edge toward \(h\), and induction forces all \(M-1\) path edges to reverse. Vertex \(k\) then forces one of the two \(sk\) edges toward \(k\). Thus

\[
\tau_{\rm canonical}=1,
\qquad
\tau_{\rm rewired}=M=2^d.
\]

For the intended isolated \(q=2\) all-one interpretation one needs \(c_2=1\), which holds for \(m\ge8\), since

\[
\frac{W}{N_2}=\frac{(m+2)(m+3)}{m(m-1)}<2.
\]

### 7.2 Literal local reachability of the rewire

**Verdict: VALID OWNERWISE.** Let \(|C|=m-3\) and

\[
s=C\cup\{x\},\quad h=C\cup\{y\},\quad k=C\cup\{z\}.
\]

For the owner

\[
X=C\cup\{x,y,z\},
\qquad(a_1,a_2,a_3)=(z,y,x),
\]

the \(q=2\) anchor is \(s\), the canonical alternate is \(h\), and a stage-\(1\) toggle carries \(z\), changing the alternate to \(k\). This is exactly an allowed same-core sibling rewire. A second owner can supply the pre-existing \(sk\) edge.

### 7.3 Missing global hypotheses

The following are **UNSUPPORTED**:

- that the stage-\(1\) toggle producing this carry is part of a globally balanced stage-\(1\) state;
- that the entire path-plus-parallel-edge component occurs and is isolated inside one exact factor;
- that external exact-factor edges cannot provide a shorter correction route;
- that this yields a counterexample to \(\mathrm{AO}_A\).

What is proved is the narrower and useful statement: within the class of abstract Johnson-supported sibling graphs, one literally allowed local rewire can have unbounded, indeed exponential, orientation recourse. Therefore Johnson adjacency and local rewiring alone supply no uniform Lipschitz recourse theorem.

## 8. Exact-factor packet identities

This is the section requiring the most important scope repair.

Fix a wreath row \(\pi\), use cyclic indices, and put \(r=m-q\). Write

\[
I_\pi(j,t)=\{\pi_j,\ldots,\pi_{j+t-1}\}.
\]

The canonical depth-\(q\) row has anchors and cores

\[
A_j=I_\pi(j,r),
\qquad C_j=I_\pi(j,r-1),
\]

and canonical alternates

\[
B_j=C_j\cup\{\pi_{j+r}\}.
\]

### 8.1 Statements surviving in every reachable \(G_q\)

**Verdict: VALID for \(r\ge2\).** Each row still contributes exactly \(n\) labelled edges; its anchors and intersections remain the canonical cyclic windows; and its owner packet remains the same packet of \(n\) middle sets.

A reachable carry in row position \(j\) has the form
\(\pi_{j+h_j}\) with

\[
r\le h_j\le m-1,
\]

so the dynamic alternate is

\[
D_j=I_\pi(j,r-1)\cup\{\pi_{j+h_j}\}.
\]

These dynamic row edges still form a matching when \(r\ge2\). Indeed, in the cyclic set \(D_j\), the complement gap following the fringe point has length
\(2m-h_j\ge m+1\), while the other separating gap has length at most
\(m-r\). The unique long gap identifies the start \(j\), after which the fringe point is identified. Hence all \(D_j\) are distinct. Each \(D_j\) has a genuine internal gap and so cannot equal a consecutive anchor \(A_k\); the anchors themselves are distinct. Thus no two row edges share an endpoint.

At the terminal rank \(r=1\), this matching proof fails and dynamic singleton alternates can collide. That rank lies outside every fixed Gaussian window for all sufficiently large \(m\).

### 8.2 Statements confined to the canonical graph

**Verdict: CORRECTED.** Only for \(H_q\), for \(G_1=H_1\), or edgewise for an unrewired owner do the **actual edge differences** form the adjacent ordered pairs of one directed coordinate Hamilton cycle and the **actual edge unions** form the cyclic \((r+1)\)-windows.

After rewiring, the actual difference pair is

\[
(\kappa_q,a_{q+1}),
\]

not the latent canonical pair \((a_q,a_{q+1})\), and the union is

\[
P_{q-1}=I_\pi(j,r)\cup\{\kappa_q\},
\]

which need not be a consecutive cyclic window. The latent deletion-word pairs
\((a_q,a_{q+1})\) still form the row's Hamilton coordinate cycle, but they are no longer the differences of rewired edges.

Thus the packet bullets in the raw report must be split as follows:

- **dynamic and canonical:** \(n\) labelled edges per row; matching for \(r\ge2\); canonical anchors; canonical intersections; fixed owner-packet partition;
- **canonical only:** actual Hamilton difference-label cycle; actual cyclic union windows;
- **dynamic replacement:** actual unions have the globally balanced histogram \(b_{q-1}\) along an admissible history, but are generally one-fringe carried sets rather than cyclic windows.

## 9. Pair-distance ledger and packetization scale

### 9.1 Exact ledger

**Verdict: VALID FOR THE LATENT/CANONICAL ROW CYCLES.** Let
\(d_\pi(x,y)\in\{1,\ldots,m\}\) be the shorter cyclic distance between
\(x,y\) in row \(\pi\). That row has exactly
\(m-d_\pi(x,y)\) middle windows containing both coordinates. Exact factorization gives

\[
\sum_{\pi\in\mathcal F}
\bigl(m-d_\pi(x,y)\bigr)
=\binom{n-2}{m-2}
=\frac{B(m-1)}2.
\]

Therefore

\[
\sum_{\pi\in\mathcal F}d_\pi(x,y)
=\frac{B(m+1)}2.
\]

If \(a\) rows make \(x,y\) adjacent, then

\[
\frac{B(m+1)}2
\le a+(B-a)m,
\]

so

\[
a\le\frac B2.
\]

This corollary constrains the canonical adjacent pairs in the latent row cycles. It does not directly bound how often an adaptive choice can use a nonadjacent carried pair
\((\kappa_q,a_{q+1})\).

### 9.2 Individual extension versus simultaneous packetization

**Verdict: VALID WITH A QUANTIFIER WARNING.** A single decorated \(q=1\) Johnson edge can be placed in a cyclic row. Since exact wreath factors exist and coordinate permutations act transitively on such decorations, that row lies in some conjugate exact factor. The conjugate may depend on the edge.

This proves

\[
\forall e\ \exists F_e\text{ containing }e,
\]

not

\[
\exists F\ \forall e\in\mathcal E\text{, }F\text{ contains all of }\mathcal E.
\]

Simultaneous inclusion of a cube or trap family, isolation, and completion of all remaining owners are **UNSUPPORTED**.

### 9.3 Scale calculation

**Verdict: VALID, WITH “TYPICAL” WEAKENED.** Since \(d\le m-1\), a largest embedded cube cycle has at most
\(2^{m-1}\) edges, while

\[
B=\frac1{2m+1}\binom{2m+1}{m}
\sim\frac{4^m}{\sqrt\pi\,m^{3/2}}.
\]

Hence \(2^{m-1}=o(B)\), so one cube is negligible on the required \(W\)-scale.

If disjoint/protected blocks of size and repair cost \(\Theta(2^d)\) are used, an \(\Omega(W)\) additive obstruction requires
\(\Omega(W/2^d)\) blocks and hence \(\Theta(W)\) prescribed owner edges. Since there are \(B\) packets of size \(n\), this is average
\(\Theta(n)\) prescribed edges per packet and forces a positive fraction of packets to carry \(\Theta(n)\) edges. It does not justify an unqualified claim about every or “typical” packet, and the additivity itself depends on genuine protection/isolation.

The sentence that a sparse partial packing “may consume all \(m+1\) odd-graph neighbours” is at most a valid warning that edge cardinality alone is not a completion theorem. No genuine partial wreath packing with that blocking property is constructed in the report, so any use of it as a formal noncompletion obstruction is **UNSUPPORTED**.

## 10. Final implication audit

The following conclusions are **VALID**:

1. Point-star Hall margins alone cannot prove the missing theorem.
2. The natural static configuration matrix is not automatically TU.
3. Johnson support, first-order point balance, and abstract Hall feasibility do not by themselves imply short supported recourse.
4. A literally allowed local carried-letter rewire can cause exponential recourse in an abstract isolated residual component.
5. Exact cyclic packetization and completion are precisely the missing bridge from those local obstructions to the exact-factor fibre.
6. The packetized higher-order Hall, packetized short-transport, exact simultaneous-integrality, and counterexample-packetization tasks listed in the report remain open.

The following conclusions are **UNSUPPORTED**:

1. existence of one exact factor containing a positive-density packing of the cube or rewire traps;
2. isolation of those traps from all remaining exact-factor edges;
3. a globally reachable balanced predecessor state for the rewire trap;
4. an \(o(W)\)-recourse theorem from the static defect bound;
5. a counterexample to \(\mathrm{SDH}_A\) or \(\mathrm{AO}_A\);
6. a proof of either theorem.

Finally, even a completed construction of one bad exact factor would not refute the existential theorem: a refutation must obstruct every factor available to the joint choice. Conversely, a positive result must remain integral inside one exact factor (or directly construct the required literal OR word). The raw report correctly stops short of either conclusion.

## 11. Audited final verdict

After the corrections above, the strongest justified statement is:

\[
\boxed{
\begin{gathered}
\text{The adaptive-state, rewiring, point-star Hall, canonical determinant,}\\
\text{abstract cube, and abstract one-rewire calculations are valid.}\\
\text{None supplies exact-factor packetization or a simultaneous recourse theorem.}\\
\mathrm{SDH}_A/\mathrm{AO}_A\text{ remains open.}
\end{gathered}}
\]
